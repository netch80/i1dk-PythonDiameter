from diameter.AVP import AVP
from diameter.Error import InvalidAVPLengthError
import struct

class AVP_Integer32(AVP):
    """32-bit signed integer AVP."""

    def __init__(self,code,value,vendor_id=0):
        AVP.__init__(self,code,struct.pack("!I",value),vendor_id)

    def queryValue(self):
        """Returns the payload as a 32-bit signed value."""
        return struct.unpack("!I",self.payload)[0]

    def setValue(self,value):
        """Sets the payload to the specified 32-bit signed value."""
        self.payload = struct.pack("!I",value)

    def __str__(self):
        return str(self.code) + ":" + str(self.queryValue())

    @staticmethod
    def narrow(avp):
        """Convert generic AVP to AVP_Integer32
        Raises: InvalidAVPLengthError
        """
        if len(avp.payload)!=4:
            raise InvalidAVPLengthError(avp)
        value = struct.unpack("!I",avp.payload)[0]
        a = AVP_Integer32(avp.code, value, avp.vendor_id)
        a.flags = avp.flags
        return a

def _unittest():
    a = AVP_Integer32(1,17)

    assert a.queryValue()==17

    a.setValue(42)
    assert a.queryValue()==42

    a = AVP_Integer32.narrow(AVP(1,"    "))
    assert a.queryValue()==0x20202020
    try:
        a = AVP_Integer32.narrow(AVP(1,"12345"))
        assert False
    except InvalidAVPLengthError:
        pass
