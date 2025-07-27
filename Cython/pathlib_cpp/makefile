# Compiler settings
CXX      := g++
CXXSTD   := c++17
CXXFLAGS := -std=$(CXXSTD) -Wall -Wextra -g
LDFLAGS  :=
LDLIBS   :=

# Project structure
SRC_DIR    := src
BUILD_DIR  := build/obj
BIN        := $(BUILD_DIR)/app

SRC_EXT    := cpp
SOURCES    := $(shell find $(SRC_DIR) -type f -name '*.$(SRC_EXT)')
OBJECTS    := $(patsubst $(SRC_DIR)/%.$(SRC_EXT),$(BUILD_DIR)/%.o,$(SOURCES))
DEPS       := $(OBJECTS:.o=.d)

# Optional inclusion/library paths
INCLUDES   :=
LIBPATHS   :=
LIBS       :=

# Debug vs Release
ifeq ($(BUILD),release)
    CXXFLAGS += -O2
else
    BUILD := debug
endif

.PHONY: all clean debug release

all: $(BIN)

dev: $(BIN)
	./$(BIN)

release: BUILD := release
release: all

debug: BUILD := debug
debug: all

$(BIN): $(OBJECTS)
	@echo "Linking $@"
	$(CXX) $(CXXFLAGS) $(OBJECTS) -o $@ $(LDFLAGS) $(LIBPATHS) $(LIBS) $(LDLIBS)

$(BUILD_DIR)/%.o: $(SRC_DIR)/%.$(SRC_EXT) | $(BUILD_DIR)
	@echo "Compiling $<"
	$(CXX) $(CXXFLAGS) $(INCLUDES) -MP -MMD -c $< -o $@

$(BUILD_DIR):
	@mkdir -p $(BUILD_DIR)

-include $(DEPS)

clean:
	@echo "Cleaning..."
	@rm -rf $(BUILD_DIR) $(BIN)
