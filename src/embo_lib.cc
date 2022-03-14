#include "embo_lib.hh"
#include <fmt/format.h>

namespace embo_lib {
    std::string greeting() {
        return fmt::format("Hello {}!", "embo++");
    }
}
