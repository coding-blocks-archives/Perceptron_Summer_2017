def avg(*args):
	return float(sum(args))/len(args)


if __name__ == '__main__':
	print avg(1, 4, 3, 2, 5)