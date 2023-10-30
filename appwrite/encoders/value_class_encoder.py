import json
from ..enums.browser import Browser
from ..enums.credit_card import CreditCard
from ..enums.flag import Flag
from ..enums.relationship_type import RelationshipType
from ..enums.relation_mutate import RelationMutate
from ..enums.index_type import IndexType
from ..enums.runtime import Runtime
from ..enums.method import Method
from ..enums.compression import Compression
from ..enums.image_gravity import ImageGravity
from ..enums.image_format import ImageFormat
from ..enums.password_version import PasswordVersion

class ValueClassEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Browser):
            return o.value

        if isinstance(o, CreditCard):
            return o.value

        if isinstance(o, Flag):
            return o.value

        if isinstance(o, RelationshipType):
            return o.value

        if isinstance(o, RelationMutate):
            return o.value

        if isinstance(o, IndexType):
            return o.value

        if isinstance(o, Runtime):
            return o.value

        if isinstance(o, Method):
            return o.value

        if isinstance(o, Compression):
            return o.value

        if isinstance(o, ImageGravity):
            return o.value

        if isinstance(o, ImageFormat):
            return o.value

        if isinstance(o, PasswordVersion):
            return o.value

        return super().default(o)