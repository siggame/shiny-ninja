sources = $(wildcard *.cpp)
headers = $(wildcard *.h)
objects = $(sources:%.cpp=%.o)
deps = $(sources:%.cpp=%.d)
CFLAGS += -g -I../c
CXXFLAGS += -g -I../c

all: client

submit: client
	@echo "$(shell cd ..;sh submit.sh cpp)"

.PHONY: clean all subdirs

clean:
	rm -f $(objects) client

client: $(objects) ../c/client.a ../c/sexp/sexp.a
	$(CXX) $(LDFLAGS) $(LOADLIBES) $(LDLIBS) $^ -g -o client

../c/client.a:
	$(MAKE) -C $(dir $@) $(notdir $@)

../c/sexp/sexp.a:
	$(MAKE) -C $(dir $@) $(notdir $@)

-include $(deps)
