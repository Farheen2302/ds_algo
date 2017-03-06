class HashMap:

	def __init__(self, size=11):
		self.size = size
		self.slots = [None]*self.size
		self.data = [None]*self.size

	def put(self, key, val):
		hash_val = self.hash(key)
		if self.slots[hash_val] == None:
			self.slots[hash_val] = key
			self.data[hash_val] = val
		else:
			if self.slots[hash_val] == key:
				self.slots[hash_val] = val
			else:
				rehash_val = self.rehash(hash_val)
				while self.slots[rehash_val] != None and self.slots[rehash_val] != key:
					rehash_val = self.rehash(rehash_val)
				if self.slots[rehash_val] == None:
					self.slots[rehash_val] = key
					self.data[rehash_val] = val
				else:
					self.data[rehash_val] = val


	def get(self, key):
		hash_val = self.hash(key)
		if self.slots[hash_val] == key:
			return self.data[hash_val]
		else:
			found = None
			done = False
			rehash_val = self.rehash(hash_val)
			while not done:
				if self.slots[rehash_val] == key:
					found = self.data[rehash_val]
					done = True
				elif rehash_val == hash_val:
					done = True
				else:
					rehash_val = self.rehash(rehash_val)
		return found


	def delete(self, key):
		hash_val = self.hash(key)
		if self.slots[hash_val] == key:
			self.slots[hash_val] = None
			self.data[hash_val] = None
		else:
			found = None
			done = False
			rehash_val = self.rehash(hash_val)
			while not done:
				if self.slots[rehash_val] == key:
					self.slots[rehash_val] = None
					self.data[rehash_val] = None
					done = True
				elif rehash_val == hash_val:
					done = True
				else:
					rehash_val = self.rehash(rehash_val)



	# def len(self):
	def __getitem__(self, key):
		return self.get(key)

	def __setitem__(self, key, data):
		self.put(key, data)

	def hash(self, key):
		return key % self.size

	def rehash(self, hash):
		return (hash + 1) % self.size

#Test Cases
H=HashMap()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
assert H[20] == 'chicken'
assert H[17] == 'tiger'
H[20]='duck'
assert H[20] == 'duck'
assert H[17] == 'tiger'
H.delete(17)
assert H[17] == None


