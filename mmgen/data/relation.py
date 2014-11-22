from mmgen.models import relationship

# Weighted list for rolling relationships
RELATION_TYPES = {
    relationship.Friend: 100,
    relationship.Parent: 40,
}
