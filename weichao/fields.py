from rest_framework.fields import CharField

class ColourField(serializers.WritableField):
    """
    Color objects are serialized into "rgb(#, #, #)" notation.
    """
    def to_native(self, obj):
        return "rgb(%d, %d, %d)" % (obj.red, obj.green, obj.blue)

    def from_native(self, data):
        data = data.strip('rgb(').rstrip(')')
        red, green, blue = [int(col) for col in data.split(',')]
        return Color(red, green, blue)
