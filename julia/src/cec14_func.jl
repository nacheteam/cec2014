function cec14_func_eval(func_number::Int, x::Array)
	res = [0.0]
	ccall((:cec14_test_func, "libs/libcec14_func"), Void,
		  (Ptr{Cdouble}, Ptr{Cdouble}, Cint, Cint, Cint),
		  x, res, length(x), 1, func_number)
	res[1]
end


function cec14_func(func_number::Int)
	f = x -> cec14_func_eval(func_number, x)
end
