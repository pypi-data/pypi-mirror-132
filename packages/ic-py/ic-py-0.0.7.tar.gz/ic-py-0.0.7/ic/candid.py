import enum
import re
from typing import AbstractSet, Any, List, Sequence
import typing
import leb128
from struct import pack,unpack
from abc import abstractclassmethod, ABCMeta
from enum import Enum
import math
from .principal import Principal as P
from .utils import labelHash

class TypeIds(Enum):
    Null = -1
    Bool = -2
    Nat = -3
    Int = -4
    Nat8 = -5
    Nat16 = -6
    Nat32 = -7
    Nat64 = -8
    Int8 = -9
    Int16 = -10
    Int32 = -11
    Int64 = -12
    Float32 = -13
    Float64 = -14
    Text = -15
    Reserved = -16
    Empty = -17
    Opt = -18
    Vec = -19
    Record = -20
    Variant = -21
    Func = -22
    Service = -23
    Principal = -24

prefix = "DIDL"

# TODO
class Pipe :
    def __init__(self, buffer = b'', length = 0):
        self._buffer = buffer
        self._view = buffer[0:len(buffer)]

    @property
    def buffer(self):
        return self._view

    @property
    def length(self):
        return len(self._view)

    @property
    def end(self) -> bool:
        return self.length == 0

    def read(self, num:int):
        if len(self._view) < num:
            raise "Wrong: out of bound"
        res = self._view[:num]
        self._view = self._view[num:]
        return res

    def readbyte(self):
        res = self._view[0]
        self._view = self._view[1:]
        return res

    def write(buf):
        pass
    
    def alloc(amount):
        pass


class ConstructType: pass
class TypeTable():
    def __init__(self) -> None:
        self._typs = []
        self._idx = {}

    def has(self, obj: ConstructType):
        return True if obj.name in self._idx else False

    def add(self, obj: ConstructType, buf):
        idx = len(self._typs)
        self._idx[obj.name] = idx
        self._typs.append(buf)

    def merge(self, obj: ConstructType, knot:str):
        idx = self._idx[obj.name] if self.has(obj) else None
        knotIdx = self._idx[knot] if knot in self._idx else None
        if idx == None:
            raise "Missing type index for " + obj.name
        if knotIdx == None:
            raise "Missing type index for " + knot
        self._typs[idx] = self._typs[knotIdx]

        #delete the type
        self._typs.remove(knotIdx)
        del self._idx[knot]

    def encode(self) :
        length = leb128.u.encode(len(self._typs))
        buf = b''.join(self._typs)
        return length + buf
    
    def indexOf(self, typeName:str) :
        if not typeName in self._idx:
            raise "Missing type index for" + typeName
        return leb128.i.encode(self._idx[typeName] | 0)


 # Represents an IDL type.
class Type(metaclass=ABCMeta):

    def display(self):
        return self.name

    def buildTypeTable(self, typeTable: TypeTable):
        if not typeTable.has(self):
            self._buildTypeTableImpl(typeTable)

    @abstractclassmethod
    def covariant(): pass

    @abstractclassmethod
    def decodeValue(): pass
    
    @abstractclassmethod
    def encodeType(): pass

    @abstractclassmethod
    def encodeValue(): pass

    @abstractclassmethod
    def checkType(): pass

    @abstractclassmethod
    def _buildTypeTableImpl(): pass

class PrimitiveType(Type):
    def __init__(self) -> None:
        super().__init__()

    def checkType(self, t: Type):
        if self.name != t.name :
            raise "type mismatch: type on the wire {}, expect type {}".format(t.name, self.name)
        return t

    def _buildTypeTableImpl(self, typeTable: TypeTable) :
        # No type table encoding for Primitive types.
        return

class ConstructType(Type, metaclass=ABCMeta):
    def __init__(self) -> None:
        super().__init__()

    def checkType(self, t: Type) -> ConstructType :
        if isinstance(t, RecClass):
            ty = t.getType()
            if ty == None:
                raise "type mismatch with uninitialized type"
            return ty
        else:
            raise "type mismatch: type on the wire {}, expect type {}".format(type.name, self.name)

    def encodeType(self, typeTable: TypeTable):  
        return typeTable.indexOf(self.name)

# Represents an IDL Empty, a type which has no inhabitants.
class EmptyClass(PrimitiveType):
    def __init__(self) -> None:
        super().__init__()

    def covariant(self):
        return False
    
    def encodeValue(self, typeTable: TypeTable):
        raise "Empty cannot appear as a function argument"

    def encodeType(self):
        return leb128.i.encode(TypeIds.Empty.value)

    def decodeValue(self):
        raise "Empty cannot appear as an output"

    @property
    def name(self) -> str:
        return 'empty'

    @property
    def id(self) -> int:
        return TypeIds.Empty.value

# Represents an IDL Bool
class BoolClass(PrimitiveType):
    def __init__(self) -> None:
        super().__init__()

    def covariant(self, x):
        return isinstance(x, bool)
    
    def encodeValue(self, val):
        return leb128.u.encode(1 if val else 0)

    def encodeType(self, typeTable: TypeTable):
        return leb128.i.encode(TypeIds.Bool.value)

    def decodeValue(self, b: Pipe, t: Type):
        self.checkType(t)
        byte = safeReadByte(b)
        if leb128.u.decode(byte) == 1:
            return True
        elif leb128.u.decode(byte) == 0:
            return False
        else:
            raise "Boolean value out of range"

    @property
    def name(self) -> str:
        return 'bool'

    @property
    def id(self) -> int:
        return TypeIds.Bool.value

# Represents an IDL Null
# check None == Null ?
class NullClass(PrimitiveType):
    def __init__(self) -> None:
        super().__init__()

    def covariant(self, x):
        return x == None
    
    def encodeValue(self):
        return b''

    def encodeType(self, typeTable: TypeTable):
        return leb128.i.encode(TypeIds.Null.value)

    def decodeValue(self, t: Type):
        self.checkType(t)
        return None

    @property
    def name(self) -> str:
        return 'null'

    @property
    def id(self) -> int:
        return TypeIds.Null.value

# Represents an IDL Reserved
class ReservedClass(PrimitiveType):
    def __init__(self) -> None:
        super().__init__()

    def covariant(self, x):
        return True
    
    def encodeValue(self):
        return b''

    def encodeType(self, typeTable: TypeTable):
        return leb128.i.encode(TypeIds.Reserved.value)

    def decodeValue(self, b: Pipe, t: Type):
        if self.name != t.name:
            t.decodeValue(b, t)
        return None

    @property
    def name(self) -> str:
        return 'reserved'

    @property
    def id(self) -> int:
        return TypeIds.Reserved.value

# Represents an IDL Text
class TextClass(PrimitiveType):
    def __init__(self) -> None:
        super().__init__()

    def covariant(self, x):
        return isinstance(x, str)
    
    def encodeValue(self, val: str):
        buf = val.encode()
        length = leb128.u.encode(len(buf))
        return  length + buf

    def encodeType(self, typeTable: TypeTable):
        return leb128.i.encode(TypeIds.Text.value)

    def decodeValue(self, b, t: Type):
        self.checkType(t)
        length = lenDecode(b)
        buf = safeRead(b, length)
        return buf.decode()

    @property
    def name(self) -> str:
        return 'text'

    @property
    def id(self) -> int:
        return TypeIds.Text.value

# Represents an IDL Int
class IntClass(PrimitiveType):
    def __init__(self) -> None:
        super().__init__()

    def covariant(self, x):
        return isinstance(x, int)
    
    def encodeValue(self, val):
        return leb128.i.encode(val)

    def encodeType(self, typeTable: TypeTable):
        return leb128.i.encode(TypeIds.Int.value)

    def decodeValue(self, b: Pipe, t: Type):
        self.checkType(t)
        return lenDecode(b)

    @property
    def name(self) -> str:
        return 'int'

    @property
    def id(self) -> int:
        return TypeIds.Int.value

# Represents an IDL Nat
class NatClass(PrimitiveType):
    def __init__(self) -> None:
        super().__init__()

    def covariant(self, x):
        return x >= 0
    
    def encodeValue(self, val):
        return leb128.u.encode(val)

    def encodeType(self, typeTable: TypeTable):
        return leb128.i.encode(TypeIds.Nat.value)

    def decodeValue(self, b: Pipe, t: Type):
        self.checkType(t)
        return lenDecode(b)

    @property
    def name(self) -> str:
        return 'nat'

    @property
    def id(self) -> int:
        return TypeIds.Nat.value

# Represents an IDL Float
class FloatClass(PrimitiveType):
    def __init__(self, _bits):
        super().__init__()
        self._bits = _bits
        if _bits != 32 and _bits != 64:
            raise "not a valid float type"

    def covariant(self, x):
        return isinstance(x, float)
    
    def encodeValue(self, val):
        if self._bits == 32:
            buf = pack('f', val)
        elif self._bits == 64:
            buf = pack('d', val)
        else:
            raise "The length of float have to be 32 bits or 64 bits "
        return buf

    def encodeType(self, typeTable: TypeTable):
        opcode = TypeIds.Float32.value if self._bits == 32 else TypeIds.Float64.value
        return leb128.i.encode(opcode)

    def decodeValue(self, b: Pipe, t: Type) -> float:
        self.checkType(t)
        by = safeRead(b, self._bits // 8)
        if self._bits == 32:
            return  unpack('f', by)[0]
        elif self._bits == 64:
            return unpack('d', by)[0]
        else:
            raise "The length of float have to be 32 bits or 64 bits "

    @property
    def name(self) -> str:
        return 'float' + str(self._bits)

    @property
    def id(self) -> int:
        return TypeIds.Float32.value if self._bits == 32 else TypeIds.Float64.value

# Represents an IDL fixed-width Int(n)
class FixedIntClass(PrimitiveType):
    def __init__(self, _bits):
        super().__init__()
        self._bits = _bits
        if _bits != 8 and _bits != 16 and \
           _bits != 32 and _bits != 64 :
           raise "bits only support 8, 16, 32, 64"

    def covariant(self, x):
        minVal = -1 * 2 ** (self._bits - 1) 
        maxVal = -1 + 2 ** (self._bits - 1) 
        if x >= minVal and x <= maxVal:
            return True
        else:
            return False
    
    def encodeValue(self, val):
        if self._bits == 8:
            buf = pack('b', val) # signed char -> Int8
        elif self._bits == 16:
            buf = pack('h', val) # short -> Int16
        elif self._bits == 32:
            buf = pack('i', val) # int -> Int32
        elif self._bits == 64:
            buf = pack('q', val) # long long -> Int64
        else:
            raise "bits only support 8, 16, 32, 64"
        return buf

    def encodeType(self, typeTable: TypeTable):
        offset = int(math.log2(self._bits) - 3)
        return leb128.i.encode(-9 - offset)

    def decodeValue(self, b: Pipe, t: Type):
        self.checkType(t)
        by = safeRead(b, self._bits // 8) 
        if self._bits == 8:
            return unpack('b', by)[0] # signed char -> Int8
        elif self._bits == 16:
            return unpack('h', by)[0] # short -> Int16
        elif self._bits == 32:
            return unpack('i', by) # int -> Int32
        elif self._bits == 64:
            return unpack('q', by) # long long -> Int64
        else:
            raise "bits only support 8, 16, 32, 64"

    @property
    def name(self) -> str:
        return 'int' + str(self._bits)

    @property
    def id(self) -> int:
        if self._bits == 8:
            return TypeIds.Int8.value
        if self._bits == 16:
            return TypeIds.Int16.value
        if self._bits == 32:
            return TypeIds.Int32.value
        if self._bits == 64:
            return TypeIds.Int64.value

# Represents an IDL fixed-width Nat(n)
class FixedNatClass(PrimitiveType):
    def __init__(self, _bits):
        super().__init__()
        self._bits = _bits
        if _bits != 8 and _bits != 16 and \
           _bits != 32 and _bits != 64 :
           raise "bits only support 8, 16, 32, 64"

    def covariant(self, x):
        maxVal = -1 + 2 ** self._bits
        if x >= 0 and x <= maxVal:
            return True
        else:
            return False
    
    def encodeValue(self, val):
        if self._bits == 8:
            buf = pack('B', val) # unsigned char -> Nat8
        elif self._bits == 16:
            buf = pack('H', val) # unsigned short -> Nat16
        elif self._bits == 32:
            buf = pack('I', val) # unsigned int -> Nat32
        elif self._bits == 64:
            buf = pack('Q', val) # unsigned long long -> Nat64
        else:
            raise "bits only support 8, 16, 32, 64"
        return buf

    def encodeType(self, typeTable: TypeTable):
        offset = int(math.log2(self._bits) - 3)
        return leb128.i.encode(-5 - offset)

    def decodeValue(self, b: Pipe, t: Type):
        self.checkType(t)
        by = safeRead(b, self._bits // 8) 
        if self._bits == 8:
            return unpack('B', by)[0] # unsigned char -> Nat8
        elif self._bits == 16:
            return unpack('H', by)[0] # unsigned short -> Nat16
        elif self._bits == 32:
            return unpack('I', by) # unsigned int -> Nat32
        elif self._bits == 64:
            return unpack('Q', by) # unsigned long long -> Nat64
        else:
            raise "bits only support 8, 16, 32, 64"

    @property
    def name(self) -> str:
        return 'nat' + str(self._bits)

    @property
    def id(self) -> int:
        if self._bits == 8:
            return TypeIds.Nat8.value
        if self._bits == 16:
            return TypeIds.Nat16.value
        if self._bits == 32:
            return TypeIds.Nat32.value
        if self._bits == 64:
            return TypeIds.Nat64.value

# Represents an IDL Array
class VecClass(ConstructType):
    def __init__(self, _type: Type):
        super().__init__()
        self._type = _type
        # If true, this vector is really a blob and we can just use memcpy.
        self._blobOptimization = False
        if isinstance(_type, FixedNatClass) and _type._bits == 8:
            self._blobOptimization = True

    def covariant(self, x):
        return type(x) == list and not False in list(map(self._type.covariant, x))
    
    def encodeValue(self, val):
        length = leb128.u.encode(len(val))
        if self._blobOptimization:
            return length + b''.join(val)
        vec = list(map(self._type.encodeValue, val))
        return length + b''.join(vec)
        
    def _buildTypeTableImpl(self, typeTable: TypeTable):
        self._type.buildTypeTable(typeTable)
        opCode = leb128.u.encode(TypeIds.Vec.value)
        buffer = self._type.encodeType(typeTable)
        typeTable.add(self, opCode + buffer)

    def decodeValue(self, b: Pipe, t: Type):
        vec = self.checkType(t)
        if not isinstance(vec, VecClass):
            raise "Not a vector type"
        length = lenDecode(b)
        if self._blobOptimization:
            return b.read(length)
        rets = []
        for _ in range(length):
            rets.append(self._type.decodeValue(b, vec._type))
        return rets

    @property
    def name(self) -> str:
        return 'vec' + str(self._type.name)

    @property
    def id(self) -> int:
        return TypeIds.Vec.value

    def display(self):
        return 'vec {}'.format(self._type.display())

# Represents an IDL Option
class OptClass(ConstructType):
    def __init__(self, _type: Type):
        super().__init__()
        self._type = _type

    def covariant(self, x):
        return type(x) == list and (len(x) == 0 | (len(x) == 1 and self._type.covariant(x[0])))
    
    def encodeValue(self, val):
        if len(val) == 0:
            return b'\x00'
        else:
            return b'\x01' + self._type.encodeValue(val[0])

    def _buildTypeTableImpl(self, typeTable: TypeTable):
        self._type.buildTypeTable(typeTable)
        opCode = leb128.u.encode(TypeIds.Opt.value)
        buffer = self._type.encodeType(typeTable)
        typeTable.add(self, opCode + buffer)

    def decodeValue(self, b: Pipe, t: Type):
        opt = self.checkType(t)
        if not isinstance(opt, OptClass):
            raise "Not an option type"
        if safeReadByte(b) == b'\x00':
            return []
        elif safeReadByte(b) == b'\x01':
            return [self._type.decodeValue(b, opt._type)]
        else:
            raise "Not an option value"

    @property
    def name(self) -> str:
        return 'opt' + str(self._type.name)

    @property
    def id(self) -> int:
        return TypeIds.Opt.value

    def display(self):
        return 'opt {}'.format(self._type.display())

# Represents an IDL Record
# todo
class RecordClass(ConstructType):
    def __init__(self, field: dict):
        super().__init__()
        self._fields = dict(sorted(field.items(), key=lambda kv: labelHash(kv[0]))) # check

    def tryAsTuple(self):
        res = []
        idx = 0
        for k, v in self._fields.items():
            if k != "_" + str(idx):
                return None
            res.append(v)
            idx += 1
        return res

    def covariant(self, x: dict):
        if type(x) != dict:
            raise "Expected dict type input."
        for k, v in self._fields.items():
            if not k in x:
                raise "Record is missing key {}".format(k)
            if v.covariant(x[k]):
                continue
            else:
                return False
        return True
    
    def encodeValue(self, val):
        bufs = []
        for k,v in self._fields.items():
            bufs.append(v.encodeValue(val[k]))
        return b''.join(bufs)


    def _buildTypeTableImpl(self, typeTable: TypeTable):
        for _, v in self._fields.items():
            v.buildTypeTable(typeTable)
        opCode = leb128.i.encode(TypeIds.Record.value)
        length = leb128.u.encode(len(self._fields))
        fields = b''
        for k, v in self._fields.items():
            fields += (leb128.u.encode(labelHash(k)) + v.encodeType(typeTable))
        typeTable.add(self, opCode + length + fields)


    def decodeValue(self, b: Pipe, t: Type):
        record = self.checkType(t)
        if not isinstance(record, RecordClass):
            raise "Not a record type"
        
        x = {}
        idx = 0
        keys = list(self._fields.keys())
        for k, v in record._fields.items() :
            if idx >= len(self._fields) or ( labelHash(keys[idx]) != labelHash(k) ):
                # skip field
                v.decodeValue(b, v)
                continue
            expectKey = keys[idx]
            exceptValue = self._fields[expectKey]
            x[expectKey] = exceptValue.decodeValue(b, v)
            idx += 1
        if idx < len(self._fields):
            raise "Cannot find field {}".format(keys[idx])
        return x

    @property
    def name(self) -> str:
        return "record"

    @property
    def id(self) -> int:
        return TypeIds.Record.value

    def display(self):
        d = {}
        for k, v in self._fields.items():
            d[v] = v.display()
        return "record {}".format(d)

# Represents Tuple, a syntactic sugar for Record.
# todo
class TupleClass(RecordClass):
    def __init__(self, *_components):
        x = {}
        for i, v in enumerate(_components):
            x['_' + str(i)] = v
        super().__init__(x)
        self._components = _components
    

    def covariant(self, x):
        if type(x) != list:
            raise "Expected list type input."
        for idx, v in enumerate(self._components):
            if v.covariant(x[idx]):
                continue
            else:
                return False
        if len(x) < len(self._fields):
            return False
        return True
    
    def encodeValue(self, val:list):
        bufs = b''
        for i in range(len(self._components)):
            bufs += self._components[i].encodeValue(val[i])
        return bufs


    def decodeValue(self, b: Pipe, t: Type):
        tup = self.checkType(t)
        if not isinstance(tup, TupleClass):
            raise "not a tuple type"
        if len(tup._components) != len(self._components):
            raise "tuple mismatch"
        res = []
        for i, wireType in enumerate(tup._components):
            if i >= len(self._components):
                wireType.decodeValue(b, wireType)
            else:
                res.append(self._components[i].decodeValue(b, wireType))
        return res

    @property
    def id(self) -> int:
        return TypeIds.Tuple.value

    def display(self):
        d = []
        for item in self._components:
            d.append(item.display())
        return "record {" + '{}'.format(';'.join(d)) + '}'

# Represents an IDL Variant
# todo
class VariantClass(ConstructType):
    def __init__(self, field):
        super().__init__()
        self._fields = dict(sorted(field.items(), key=lambda kv: labelHash(kv[0]))) # check
        

    def covariant(self, x):
        if len(x) != 1:
            return False
        for k, v in self._fields.items():
            if not k in x or v.covariant(x[k]):
                continue
            else:
                return False
        return True
    
    def encodeValue(self, val):
        idx = 0
        for name, ty in self._fields.items():
            if name in val:
                count = leb128.i.encode(idx)
                buf = ty.encodeValue(val[name])
                return count + buf
            idx += 1
        raise "Variant has no data: {}".format(val) 

    def _buildTypeTableImpl(self, typeTable: TypeTable):
        for _, v in self._fields.items():
            v.buildTypeTable(typeTable)
        opCode = leb128.i.encode(TypeIds.Variant.value)
        length = leb128.u.encode(len(self._fields))
        fields = b''
        for k, v in self._fields.items():
            fields += leb128.u.encode(labelHash(k)) + v.encodeType(typeTable)
        typeTable.add(self, opCode + length + fields)


    def decodeValue(self, b: Pipe, t: Type):
        variant = self.checkType(t)
        if not isinstance(variant, VariantClass):
            raise "Not a variant type"
        idx = lenDecode(b)
        if idx >= len(variant._fields):
            raise "Invalid variant index: {}".format(idx)
        keys = list(variant._fields.keys())
        wireHash = keys[idx]
        wireType = variant._fields[wireHash]

        for key, expectType in self._fields.items():
            if labelHash(wireHash) == labelHash(key):
                ret = {}
                value = expectType.decodeValue(b, wireType)
                ret[key] = value
                return ret
        raise "Cannot find field hash {}".format(wireHash)


    @property
    def name(self) -> str:
        # return 'variant {}'.format(self._fields)
        return 'variant'

    @property
    def id(self) -> int:
        return TypeIds.Variant.value

    def display(self):
        d = {}
        for k, v in self._fields.items():
            d[k] = '' if v.name == None else v.name
        return 'variant {}'.format(d)

# Represents a reference to an IDL type, used for defining recursive data types.
class RecClass(ConstructType):
    _counter = 0
    def __init__(self):
        super().__init__()
        self._id = RecClass._counter
        RecClass._counter += 1
        self._type = None

    def fill(self, t: ConstructType):
        self._type = t
    
    def getType(self):
        return self._type
    
    def covariant(self, x):
        return self._type if self._type.covariant(x) else False
    
    def encodeValue(self, val):
        if self._type == None:
            raise "Recursive type uninitialized"
        else:
            return self._type.encodeValue(val)

    def _buildTypeTableImpl(self, typeTable: TypeTable):
        if self._type == None:
            raise "Recursive type uninitialized"
        else:
            typeTable.add(self, b'') # check b'' or []
            self._type.buildTypeTable(typeTable)
            typeTable.merge(self, self._type.name)


    def decodeValue(self, b: Pipe, t: Type):
        if self._type == None:
            raise "Recursive type uninitialized"
        else:
            return self._type.decodeValue(b, t)

    @property
    def name(self) -> str:
        return 'rec_{}'.format(self._id)


    def display(self):
        if self._type == None:
            raise "Recursive type uninitialized"
        else:
            return 'μ{}.{}'.format(self.name, self._type.name)
        
# Represents an IDL principal reference
class PrincipalClass(PrimitiveType):
    def __init__(self) -> None:
        super().__init__()

    def covariant(self, x):
        if isinstance(x,str):
            p = P.from_str(x)
        elif isinstance(x, bytes):
            p = P.from_hex(x.hex())
        else:
            raise "only support string or bytes format"
        return p.isPrincipal

    
    def encodeValue(self, val):
        tag = int.to_bytes(1, 1, byteorder='big')
        if isinstance(val, str):
            buf = P.from_str(val).bytes
        elif isinstance(val, bytes):
            buf = val
        else:
            raise "Principal should be string or bytes."
        l = leb128.u.encode(len(buf))
        return tag + l + buf

    def encodeType(self,typeTable: TypeTable):
        return leb128.i.encode(TypeIds.Principal.value)

    def decodeValue(self, b: Pipe, t: Type):
        self.checkType(t)
        res = safeReadByte(b)
        if leb128.u.decode(res) != 1:
            raise "Cannot decode principal"
        length = lenDecode(b)
        return P.from_hex(safeRead(b, length).hex())

    @property
    def name(self) -> str:
        return 'principal'       

    @property
    def id(self) -> int:
        return TypeIds.Principal.value

# TODO class FunClass and ServiceClass

# through Pipe to decode bytes
def lenDecode(pipe: Pipe):
    weight = 1
    value = 0
    while True:
        byte = safeReadByte(pipe)
        value += (leb128.u.decode(byte) & 0x7f) * weight
        weight = weight << 7
        if byte < b'\x80' or pipe.length == 0:
            break
    return value
            
        
def safeRead(pipe: Pipe, num:int):
    if pipe.length < num:
        raise "unexpected end of buffer"
    return pipe.read(num)

def safeReadByte(pipe: Pipe):
    if pipe.length < 1:
        raise "unexpected end of buffer"
    return pipe.read(1)

def readTypeTable(pipe):
    #types length
    typeTable = []
    typeTable_len = lenDecode(pipe)
    # contruct type todo
    for _ in range(typeTable_len):
        ty = leb128.i.decode(safeReadByte(pipe))
        if ty == TypeIds.Opt.value or ty == TypeIds.Vec.value:
            t = leb128.i.decode(safeReadByte(pipe))
            typeTable.append([ty, t])
        elif ty == TypeIds.Record.value or ty == TypeIds.Variant.value:
            fields = []
            objLength = lenDecode(pipe)
            prevHash = -1
            for _ in range(objLength):
                hash = lenDecode(pipe)
                if hash >= math.pow(2, 32):
                    raise "field id out of 32-bit range"
                if type(prevHash) == int and prevHash >= hash:
                    raise "field id collision or not sorted"
                prevHash = hash
                t = leb128.i.decode(safeReadByte(pipe))
                fields.append([hash, t])
            typeTable.append([ty, fields])
        elif ty == TypeIds.Func.value:
            # TODO
            pass
        elif ty == TypeIds.Service.value:
            # TODO
            pass
        else:
            raise "Illegal op_code: {}".format(ty)
        
    rawList = []
    types_len = lenDecode(pipe)
    for _ in range(types_len):
        rawList.append(leb128.i.decode(safeReadByte(pipe)))
    return typeTable, rawList

def getType(rawTable, table, t:int) -> Type :
    idl = Types()
    if t < -24: 
        raise "not supported type"
    if t < 0:
        if   t == -1:
            return idl.Null
        elif t == -2:
            return idl.Bool
        elif t == -3:
            return idl.Nat
        elif t == -4:
            return idl.Int
        elif t == -5:
            return idl.Nat8
        elif t == -6:
            return idl.Nat16
        elif t == -7:
            return idl.Nat32
        elif t == -8:
            return idl.Nat64
        elif t == -9:
            return idl.Int8
        elif t == -10:
            return idl.Int16
        elif t == -11:
            return idl.Int32
        elif t == -12:
            return idl.Int64
        elif t == -13:
            return idl.Float32
        elif t == -14:
            return idl.Float64
        elif t == -15:
            return idl.Text
        elif t == -16:
            return idl.Reserved
        elif t == -17:
            return idl.Empty
        elif t == -24:
            return idl.Principal
        else:
            raise "Illegal op_code:{}".format(t)
    if t >= len(rawTable):
        raise "type index out of range" 
    return table[t]


def buildType(rawTable, table, entry):
    ty = entry[0]
    if ty == TypeIds.Vec.value:
        if ty >= len(rawTable):
            raise "type index out of range"
        t = getType(rawTable, table, entry[1])
        if t == None:
            t = table[t]
        return Types.Vec(t)
    elif ty == TypeIds.Opt.value:
        if ty >= len(rawTable):
            raise "type index out of range"
        t = getType(rawTable, table, entry[1])
        if t == None:
            t = table[t]
        return Types.Opt(t)
    elif ty == TypeIds.Record.value:
        fields = {}
        for hash , t in entry[1]:
            name = '_' + str(hash)
            if t >= len(rawTable):
                raise "type index out of range"
            temp = getType(rawTable, table, t)
            fields[name] = temp
        record = Types.Record(fields)
        tup = record.tryAsTuple()
        if type(tup) == list:
            return Types.Tuple(*tup)
        else:
            return record
    elif ty == TypeIds.Variant.value:
        fields = {}
        for hash , t in entry[1]:
            name = '_' + str(hash)
            if t >= len(rawTable):
                raise "type index out of range"
            temp = getType(rawTable, table, t)
            fields[name] = temp
        return Types.Variant(fields)
    # elif TypeIds.Func.value:
    #     return Types.Func([], [], [])
    # elif TypeIds.Service.value:
    #     return Types.Service({})
    else:
        raise "Illegal op_code: {}".format(ty)
    


# params = [{type, value}]
# data = b'DIDL' + len(params) + encoded types + encoded values
def encode(params):
    argTypes = []
    args = []
    for p in params:
        argTypes.append(p['type'])
        args.append(p['value'])
    # argTypes: List, args: List
    if len(argTypes) != len(args):
        raise "Wrong number of message arguments"
    typetable = TypeTable()
    for item in argTypes:
        item.buildTypeTable(typetable)
    
    pre = prefix.encode()
    table = typetable.encode()
    length = leb128.u.encode(len(args))
    
    typs = b''
    for t in argTypes:
        typs += t.encodeType(typetable)
    vals = b''
    for i in range(len(args)):
        t = argTypes[i]
        if not t.covariant(args[i]):
            raise "Invalid {} argument: {}".format(t.display(), str(args[i]))
        vals += t.encodeValue(args[i])
    return pre + table + length + typs + vals

# decode a bytes value
# def decode(retTypes, data):
def decode(data, retTypes=None):
    b = Pipe(data)
    if len(data) < len(prefix):
        raise "Message length smaller than prefix number"
    prefix_buffer = safeRead(b, len(prefix)).decode()
    if prefix_buffer != prefix:
        raise "Wrong prefix:" + prefix_buffer + 'expected prefix: DIDL'
    rawTable, rawTypes = readTypeTable(b)
    if retTypes:
        if type(retTypes) != list:
            retTypes = [retTypes]
        if len(rawTypes) < len(retTypes):
            raise "Wrong number of return value"
    
    table = []
    for _ in range(len(rawTable)):
        table.append(Types.Rec())

    for i, entry in enumerate(rawTable):
        t = buildType(rawTable, table, entry)
        table[i].fill(t)

    types = []
    for t in rawTypes:
        types.append(getType(rawTable, table, t))
    outputs = []
    for i, t in enumerate(types):
        outputs.append({
            'type': t.name,
            'value': t.decodeValue(b, types[i])
            })

    return outputs

class Types():
    Null = NullClass()
    Empty = EmptyClass()
    Bool = BoolClass()
    Int = IntClass()
    Reserved = ReservedClass()
    Nat = NatClass()
    Text = TextClass()
    Principal = PrincipalClass()
    Float32 =  FloatClass(32)
    Float64 =  FloatClass(64)
    Int8 =  FixedIntClass(8)
    Int16 =  FixedIntClass(16)
    Int32 =  FixedIntClass(32)
    Int64 =  FixedIntClass(64)
    Nat8 =  FixedNatClass(8)
    Nat16 =  FixedNatClass(16)
    Nat32 =  FixedNatClass(32)
    Nat64 =  FixedNatClass(64)

    def Tuple(*types):
        return TupleClass(*types)

    def Vec(t):
        return VecClass(t)

    def Opt(t):
        return OptClass(t)

    def Record(t):
        return RecordClass(t)

    def Variant(fields):
        return VariantClass(fields)
    
    def Rec():
        return RecClass()

    # not supported yet
    '''
    def Func(args, ret, annotations):
        return FuncClass(args, ret, annotations)
    def Service(t):
        return ServiceClass(t)
    '''



if __name__ == "__main__":
    # nat = NatClass()
    # res1 = encode([{'type':nat, 'value':10000000000}])
    # print('res1:'+ res1.hex())

    # principal = PrincipalClass()
    # res2 = encode([{'type': principal, 'value':'aaaaa-aa'}])
    # print('res2' + res2.hex())

    # res = encode([{'type': principal, 'value':'aaaaa-aa'},{'type':nat, 'value':10000000000}])
    # print('res:' + res.hex())

    # data = b'DIDL\x00\x01q\x08XTC Test'
    # print('decode data: {}'.format(data))
    # out = decode(data)
    # print(out)

    # data = b'DIDL\x00\x01}\xe2\x82\xac\xe2\x82\xac\xe2\x80'
    # print('decode data: {}'.format(data))
    # out = decode(data)
    # print(out)

    # record
    # record = Types.Record({'foo':Types.Text, 'bar': Types.Int})
    # res = encode([{'type': record, 'value':{'foo': '💩', 'bar': 42}}])
    # print('expected:', '4449444c016c02d3e3aa027c868eb7027101002a04f09f92a9')
    # print('current:', res.hex())
    # print(decode(record, res))

    # tuple(Int, Nat)
    # tup = Types.Tuple(Types.Int, Types.Text)
    # res = encode([{'type': tup, 'value': [42, '💩']}])
    # print('expected:', '4449444c016c02007c017101002a04f09f92a9')
    # print('current:', res.hex())
    # print(decode(tup, res))

    # variant
    # tup = Types.Variant({'ok': Types.Text, 'err': Types.Text})
    # res = encode([{'type': tup, 'value': {'ok': 'good'} }])
    # print('expected:', '4449444c016b03017e9cc20171e58eb4027101000104676f6f64')
    # print('current:', res.hex())
    # print(decode(tup, res))
    
    # tuple(variant)
    # tup = Types.Tuple(Types.Variant({'ok': Types.Text, 'err': Types.Text}))
    # res = encode([{'type': tup, 'value': [{'ok': 'good'}] }])
    # print('expected:', '4449444c026b029cc20171e58eb402716c01000001010004676f6f64')
    # print('current:', res.hex())
    # print(decode(tup, res))
    ty = Types.Variant({'ok': Types.Nat, 'err': Types.Variant})
    data = b'DIDL\x02k\x02\x9c\xc2\x01}\xe5\x8e\xb4\x02\x01k\x03\xb5\xda\x9a\xa3\x03\x7f\xb9\xd6\xc8\x94\x06\x7f\xd4\xb4\xc5\x9a\t\x7f\x01\x00\x00\x9e\x01'
    print(decode(ty, data))
