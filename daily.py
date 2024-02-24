class UnionFind:
  def __init__(self, n: int):
    self.id = list(range(n))
    self.rank = [0] * n

  def unionByRank(self, u: int, v: int) -> None:
    i = self._find(u)
    j = self._find(v)
    if i == j:
      return
    if self.rank[i] < self.rank[j]:
      self.id[i] = j
    elif self.rank[i] > self.rank[j]:
      self.id[j] = i
    else:
      self.id[i] = j
      self.rank[j] += 1

  def connected(self, u: int, v: int) -> bool:
    return self._find(self.id[u]) == self._find(self.id[v])

  def reset(self, u: int) -> None:
    self.id[u] = u

  def _find(self, u: int) -> int:
    if self.id[u] != u:
      self.id[u] = self._find(self.id[u])
    return self.id[u]


class Solution:
  def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
    uf = UnionFind(n)
    timeToPairs = collections.defaultdict(list)

    uf.unionByRank(0, firstPerson)

    for x, y, time in meetings:
      timeToPairs[time].append((x, y))

    for _, pairs in sorted(timeToPairs.items(), key=lambda x: x[0]):
      peopleUnioned = set()
      for x, y in pairs:
        uf.unionByRank(x, y)
        peopleUnioned.add(x)
        peopleUnioned.add(y)
      for person in peopleUnioned:
        if not uf.connected(person, 0):
          uf.reset(person)

    return [i for i in range(n) if uf.connected(i, 0)]






#  question 2

class Solution:
  def buyChoco(self, prices: List[int], money: int) -> int:
    min1 = math.inf
    min2 = math.inf

    for price in prices:
      if price <= min1:
        min2 = min1
        min1 = price
      elif price < min2:
        min2 = price

    minCost = min1 + min2
    return money if minCost > money else money - minCost