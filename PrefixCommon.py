class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        prefix = strs[0] # Recebe a primeira string inteira
        
        for s in strs[1:]: # Percorre as outras strings da lista
             while not s.startswith(prefix) and prefix: # Enquanto a string 's' não começar com o prefixo...
                    prefix = prefix[:-1]     # ...diminui o prefixo em uma letra no final! 
                    

        return prefix

        """ Simulando: teste, testa, tentativa
        
        A primeira recebe teste.
        Compara ela começa com testa, tentativa...
         Se é igual, retorna o prefixo, senão, como neste caso
            Tira um letra do teste-> test
        Compara se test começa com testa, tentativa
         Se sim, retorna o prefixo test
        
        """