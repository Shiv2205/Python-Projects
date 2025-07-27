#include <iostream>
#include <sys/stat.h>
#include "pathlib_cpp.hpp"

int main() {

  Path p("./src/main.cpp");
  Path hl("./src/HL.cpp");

  std::cout << p.exists() << std::endl;
  std::cout << hl.exists() << std::endl;

  return 0;
}
