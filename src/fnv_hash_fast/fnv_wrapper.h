

#include <stdint.h>

// https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function
uint32_t _c_fnv1a_32(const unsigned char *data) {
    unsigned char *s = (unsigned char *)data;
    uint32_t hash = ((uint32_t)0x811c9dc5);
    while (*s) {
        hash ^= (uint32_t)*s++;
        hash += (hash<<1) + (hash<<4) + (hash<<7) + (hash<<8) + (hash<<24);
    }
    return hash;
}
