def boostrap(sample, sample_size, iterations):
	# <---INSERT YOUR CODE HERE--->
	s_array = np.empty((iterations,sample_size))

	for i in iterations:
		for s in sample_size:
			s_array[i,s] = random.choice(sample)
		data_mean[i] = np.mean(s_array)

	lower = np.percentile(data_mean,2.5)
	upper = np.percentile(data_mean,97.5)

	return data_mean, lower, upper