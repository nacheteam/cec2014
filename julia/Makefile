LIB=libs
SRC=src


$(LIB)/libcec14_func.so: $(SRC)/cec14_func.c
	mkdir -p $(LIB)
	c99 -g -shared -fPIC -Wl,-soname,cec14_func.so -o $@ $^ -lc
