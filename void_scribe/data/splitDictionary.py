import pickle
# import names as nms

# data = nms.names
save_directory = r"C:\\Users\\thepe_000\\Desktop\\PP5\VoidScribe\\void_scribe\\data\\Names\\"

# for key in data:
#     save = data[key]
#     pickle.dump(save, open(save_directory + key + ".p", "wb"))

#from Names import americanCities

test_1 = pickle.load(open(save_directory + 'americanCities' + ".p", "rb" ))
#test_2 = pickle.loads(americanCities)

print(test_1)
#print(test_2)






