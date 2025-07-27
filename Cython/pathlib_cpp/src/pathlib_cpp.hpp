#ifndef PATHLIB_CPP_H
#define PATHLIB_CPP_H

#include <filesystem>
#include <string>

namespace fs = std::filesystem;

typedef std::string string;

class Path {
public:
  Path(string path = "");

  bool exists() {
    return fs::exists(this->p);
  }

private:
  fs::path p;
};

#endif //PATHLIB_CPP_H
