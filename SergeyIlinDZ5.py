class Sequence (object):
    def __init__(self, string : str) -> None:
        self.sequence = string  

    def transcribe(self)->None: 
        raise NameError
    
class DNA (Sequence):
    def count_nucleotides(self) -> dict:
        A = self.sequence.count('A')
        T = self.sequence.count('T')
        G = self.sequence.count('G')
        C = self.sequence.count('C')
        self.count = {'A': A, 'T': T, 'G': G, 'C': C}
        return self.count
    
    def transcribe(self) -> str:
        self.string_RNA = self.sequence.replace('T', 'U')
        return self.string_RNA
    
    def complement_dna(self) -> str:
        self.string_cmpl = self.sequence
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

        if len(self.sequence) == len(string2):
            diff_count = 0
            for i in range(0, len(self.sequence)):
                if self.sequence[i] != string2[i]:
                    diff_count += 1
            self.hammdist = diff_count
        else: diff_count = ('Молекулы разной длины. Операция невозможна')

        return self.hammdist


class RNA(Sequence):
    def transcribe(self) -> str:
        self.string_tr = self.sequence.replace('U', 'T')
        return self.string_tr
    def count_nucleotides(self) -> dict:
        A = self.sequence.count('A')
        U = self.sequence.count('U')
        G = self.sequence.count('G')
        C = self.sequence.count('C')
        self.count = {'A': A, 'U': U, 'G': G, 'C': C}
        return self.count

cl = DNA(input('Введите последовательность ДНК '))
cl.count_nucleotides()
cl.transcribe()
cl.complement_dna()
cl.hamming_distance(input('Введите вторую последовательность ДНК '))
print (cl.count, cl.string_RNA, cl.string_cmpl, cl.hammdist)

r = RNA(input('Введите последовательность РиНК '))
r.transcribe()
print(r.string_tr)