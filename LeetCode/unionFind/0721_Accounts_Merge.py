class Solution:
    """
    @param accounts: List[List[str]]
    @return: return a List[List[str]]
    """
    def initialize(self, accounts):
        # father dic store all father id for each id(index of account), default to itself
        self.father = {}
        for i in range(len(accounts)):
            self.father[i] = i
    
    def union(self, son, dad):
        self.father[self.find(son)] = self.find(dad)
        
    def find(self, id):
        # to find the highest father whos father is itself
        # point all id in path to that father
        path = []
        curId = id
        while self.father[curId] != curId:
            path.append(curId)
            # climb up 1 step
            curId = self.father[curId]
            
        for members in path:
            self.father[members] = curId
            
        return curId
        
    def mapEmailToIdList(self, accounts):
        emailIdListDic = {}
        for idx, account in enumerate(accounts):
            for email in account[1:]:
                emailIdListDic[email] = [*emailIdListDic.get(email, []), idx]
        return emailIdListDic
        
    def unionIdsWithSameEmail(self, emailIdListDic):
        for email, idList in emailIdListDic.items():
            rootId = idList[0]
            # if only 1 element, skip
            for id in idList[1:]:
                self.union(rootId, id)
        
    def mapIdToEmailSet(self, accounts):
        idEmailSetDic = {}
        for idx, account in enumerate(accounts):
            rootUserId = self.find(idx)
            updatedIdEmailSet = idEmailSetDic.get(rootUserId, set())
            for email in account[1:]:
                updatedIdEmailSet.add(email)
            idEmailSetDic[rootUserId] = updatedIdEmailSet
        return idEmailSetDic
    
    def accountsMerge(self, accounts):
        # write your code here
        self.initialize(accounts)
        
        emailIdListDic = self.mapEmailToIdList(accounts)
        
        self.unionIdsWithSameEmail(emailIdListDic)
        
        idEmailSetDic = self.mapIdToEmailSet(accounts)
        
        mergedAccounts = [[accounts[id][0], *sorted(idEmailSetDic[id])] for id in idEmailSetDic.keys()]
        
        return mergedAccounts
            
