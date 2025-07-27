#include "pathlib_cpp.hpp"
#include <filesystem>

Path::Path(string path) {
  this->p = fs::path(path);
}
