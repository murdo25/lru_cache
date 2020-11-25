# Notes:
# When adding new keys that cause the capacity to be exceeded, the “least recently used”
# key needs to be identified and discarded.
# Both reading and writing the value of a key are considered the use of that key


class LRUC:
	def __init__(self, max_size):
		self.max_size = max_size
		self.keys = {} 
		self.items = []

	def put(self, key, value):
		if(key in self.keys):
			self.delete(key)
		else:
			if(len(self.items)+1 > self.max_size):
				k = self.items.pop()
				del self.keys[k]
		self.keys[key] = value
		self.items.insert(0,key)

	# get the value of a key.
	def get_value(self, key):
		if(key in self.keys):
			value = self.keys[key]
			self.delete(key)
			self.keys[key] = value
			self.items.insert(0,key)
			return value
		return None
	
	# delete a key (attempting to delete a key that doesn't exist is a no-op)
	def delete(self, key):
		if key in self.keys:
			for i in range(len(self.items)):
				if(self.items[i] == key):
					del self.items[i]
					break
			del self.keys[key]

	# remote all items from the cache
	def reset(self):
		self.items = []
		self.keys = {}
		return


size = 3 
lruc = LRUC(size)

# for fun I'm going to be playing with names and ages <(00,)>
# Name, age
# ben , 25
# sam , 22
# joe , 45
# cay , 23
# squ , 29

lruc.put("ben",25)
lruc.put("ben",25)

# check to make sure we don't allow duplicates
assert len(lruc.items) == 1, "too many items"
assert len(lruc.keys) == 1, "too many keys"

lruc.put("sam", 22)

# check to make sure we don't 
assert lruc.items[0] == "sam", "wrong order of items"
assert lruc.get_value("sam") == 22, "wrong value"
assert lruc.get_value("ASDF") == None, "wrong value"

lruc.get_value("ben")
lruc.put("joe", 45)
assert lruc.items[0] == "joe", "wrong order"
lruc.get_value("ben")
assert lruc.items[1] == "joe", "wrong order"
lruc.put("cay", 23)
assert lruc.items[2] == "joe", "wrong order"
lruc.get_value("ben")
lruc.put("squ", 28)
assert lruc.get_value("joe") == None, "wrong total size"
lruc.get_value("ben")

assert lruc.items[0] == "ben", "wrong order"
assert len(lruc.items) <= size, "size does not match the max_size"

lruc.reset()
assert len(lruc.items) == 0, "reset failed"
assert len(lruc.keys) == 0, "reset failed"

print("Finished! :D")




