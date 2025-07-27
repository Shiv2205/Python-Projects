#include <filesystem>
#include <iostream>
#include <sys/stat.h>
#include "pathlib_cpp.hpp"

#define LOG(msg) (std::cout << (msg) << std::endl)

int main() {
  string p = "./src/main.cpp";
  string hl = "./src/hl.cpp";

  fs::path sys_path(p);
  fs::path abs_path(resolve(sys_path));
  vector<string> path_parts = parts(abs_path);
  vector<fs::path> path_parents = parents(abs_path); // TODO: REPAIR

  std::cout << "==================== START OF TESTING ZONE ====================================" << std::endl;

  std::cout << exists(p) << std::endl;
  LOG(resolve(abs_path));

  for (auto& part : path_parts){
    std::cout << part << ", ";
  }

  LOG(drive(abs_path));
  LOG(root(abs_path));
  LOG(parent(abs_path).string());

  LOG("\n");

  for (auto& p : path_parents) {
    LOG(p.string()); 
  }

  LOG("\n");
  LOG(name(abs_path));
  LOG(name(parent(abs_path)));

  LOG("\n");
  fs::path ext("./src/smth.tar.gz");
  LOG(suffix(ext));
  LOG(stem(ext));

  return 0;
}
