class DNA (object):
    def __init__(self, string: str) -> None:
        self.string = string

    def count_nucleotides(self) -> dict:
        A = self.string.count ('A')
        T = self.string.count ('T')
        G = self.string.count ('G')
        C = self.string.count ('C')
        self.count = {'A': A, 'T': T, 'G': G, 'C': C}
        return self.count
    
    def transcribe(self) -> str:
        self.string_RNA = self.string.replace('T', 'U')
        return self.string_RNA
    
    def complement_dna(self) -> str:
        self.string_cmpl = self.string
        self.string_cmpl = self.string_cmpl.replace('A', '1')
        self.string_cmpl = self.string_cmpl.replace('T', '2')
        self.string_cmpl = self.string_cmpl.replace('G', '3')
        self.string_cmpl = self.string_cmpl.replace('C', '4')
        self.string_cmpl = self.string_cmpl.replace('1', 'T')
        self.string_cmpl = self.string_cmpl.replace('2', 'A')
        self.string_cmpl = self.string_cmpl.replace('3', 'C')
        self.string_cmpl = self.string_cmpl.replace('4', 'G')
        return self.string_cmpl

    def hamming_distance(self, string2 : str) -> int:

        if len(self.string) == len(string2):
            diff_count = 0
            for i in range(0, len(self.string)):
                if self.string[i] != string2[i]:
                    diff_count += 1
            self.hammdist = diff_count
        else: diff_count = ('Молекулы разной длины. Операция невозможна')

        return self.hammdist


class RNA(object):
    def __init__(self, string : str) -> None:
        self.string = string
    
    def transcribe(self) -> str:
        self.string_tr = self.string.replace('U', 'T')
        return self.string_tr

cl = DNA('AAATTTGGGCCC')
cl.count_nucleotides()
cl.transcribe()
cl.complement_dna()
cl.hamming_distance('AAAGGGTTTCCC')
print (cl.count, cl.string_RNA, cl.string_cmpl, cl.hammdist)

r = RNA('AAAUUUGGGCCC')
r.transcribe()
print(r.string_tr)