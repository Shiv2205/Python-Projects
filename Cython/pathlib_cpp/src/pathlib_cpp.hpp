#ifndef PATHLIB_CPP_H
#define PATHLIB_CPP_H

#include <filesystem>
#include <iostream>
#include <string>
#include <vector>

namespace fs = std::filesystem;

using string = std::string;
template <typename T>
using vector = std::vector<T>;

inline bool exists(const fs::path& sys_path) {
  return fs::exists(sys_path);
}

inline bool exists(const string& sys_path) {
  return fs::exists(fs::path(sys_path));
}

inline fs::path resolve(const fs::path& sys_path) {
  return fs::canonical(fs::absolute(sys_path));
}

inline vector<string> parts(const fs::path& sys_path) {
  vector<string> path_parts = {};
  for (const auto& part : sys_path) {
    path_parts.push_back(part.string());
  }

  return path_parts;
}

inline string drive(const fs::path& sys_path) {
  return sys_path.root_name().string();
}

inline string root(const fs::path& sys_path) {
  return sys_path.root_directory().string();
}

inline string anchor(const fs::path& sys_path) {
  return sys_path.root_path().string();
}

inline fs::path parent(const fs::path& sys_path) {
  return sys_path.parent_path();
}

inline vector<fs::path> parents(const fs::path& sys_path) {
  vector<fs::path> path_parents = {};
  fs::path curr_path = sys_path;
  string path_root = root(sys_path);

  while (curr_path.string() != path_root) {
    path_parents.push_back((curr_path = parent(curr_path)));
  }
  
  return path_parents;
}

inline string name(const fs::path& sys_path) {
  if (sys_path.empty() || fs::is_directory(sys_path)) {
    return "";
  }
  return sys_path.filename().string();
}

inline string suffix(const fs::path& sys_path) {
  return sys_path.extension();
}

inline string stem(const fs::path& sys_path) {
  return sys_path.stem().string();
}

inline bool is_absolute(const fs::path& sys_path) {
  return sys_path.is_absolute();
}

#endif //PATHLIB_CPP_H
