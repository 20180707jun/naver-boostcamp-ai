import random
random.seed(10)

def cal_fitness(queens):
    l = len(queens)
    fit_cnt = 0
    for i in range(l):
        for j in range(i+1, l):
            x_i, y_i = queens[i]
            x_j, y_j = queens[j]
            if x_i!=x_j and y_i!=y_j and abs((y_i-y_j)/(x_i-x_j))!=1:
                fit_cnt += 1     
    return fit_cnt

def is_solution(max_score, board_size):
    solution_num = (board_size*(board_size-1))//2
    if max_score==solution_num:
        return True
    else:
        return False
    

class Genetic:
    def __init__(self, board_size, gene_num):
        self.generation = 1
        self.board_size = board_size
        self.gene_num = gene_num
        self.genes = [[(i, random.randrange(1, board_size+1)) for i in range(1, board_size+1)] \
                     for _ in range(gene_num)]
        self.next_generation_candidate = []


    def selection(self, select_num=None):
        if select_num==None:
            select_num = self.gene_num
        self.select_num = select_num
        scores = list(map(cal_fitness, self.genes))
        m_score = max(scores)
        m_idx = scores.index(m_score)
        m_gene = self.genes[m_idx]
        self.next_generation_candidate = random.choices(self.genes, weights=scores, k=select_num)
        return scores, m_gene
        
    def crossover(self, p=0.5):
        p = p/2
        n = int(self.select_num*p)
        pick_nums = random.sample(range(self.select_num), k=n*2)
        for i in range(n):
            cross_point = random.randrange(1, self.board_size+1)
            
            idx1 = pick_nums[i*2]
            idx2 = pick_nums[i*2+1]
                             
            tar1 = [y for x, y in self.genes[idx1]]
            tar2 = [y for x, y in self.genes[idx2]]
            new_tar1 = tar1[:cross_point] + tar2[cross_point:]
            new_tar2 = tar1[cross_point:] + tar2[:cross_point]
            self.next_generation_candidate[idx1] = [(x, y) for x, y in enumerate(new_tar1, start=1)]
            self.next_generation_candidate[idx2] = [(x, y) for x, y in enumerate(new_tar2, start=1)]
            
    def mutation(self, theta=0.5):
        for gene_idx in range(self.select_num):
            for info_idx in range(self.board_size):
                if random.random()<theta:
                    mut_num = random.randrange(1, self.board_size+1)
                    self.next_generation_candidate[gene_idx][info_idx] = (info_idx+1, mut_num)
    
    def replacement(self, rep_p=0.5):
        rep_num = int(rep_p*self.gene_num)
        next_genes = []
        genes_scores = list(map(cal_fitness, self.genes))
        next_genes_scores = list(map(cal_fitness, self.next_generation_candidate))
        genes_scores = [(score, i) for i, score in enumerate(genes_scores)]
        next_genes_scores = [(score, i) for i, score in enumerate(next_genes_scores)]

        genes_scores.sort(reverse=True)
        next_genes_scores.sort(reverse=True)

        for i in range(rep_num):
            score, next_gene_idx = next_genes_scores[i]
            next_genes.append(self.next_generation_candidate[next_gene_idx])
        for i in range(self.gene_num-rep_num):
            score, next_gene_idx = genes_scores[i]
            next_genes.append(self.genes[next_gene_idx])
        self.genes = next_genes
        self.next_generation_candidate = []

    def generate(self, cross_p=0.5, mutation_p=0.5, rep_p=0.5):
        scores, m_gene = self.selection()
        self.crossover(p=cross_p)
        self.mutation(theta=mutation_p)
        self.replacement(rep_p=rep_p)
        self.generation += 1
        return max(scores), m_gene

    def generate_ntimes(self, iteration, cross_p=0.5, mutation_p=0.5, rep_p=0.5, print_several_times=100):
        for i in range(iteration):
            m_score, m_gene = self.generate(cross_p, mutation_p, rep_p)
            if is_solution(m_score, self.board_size):
                print(f"{i} generation's solotion : {m_gene}")
            if self.generation%print_several_times==0:
                print(f'{self.generation} generation \
                    max score : {m_score}, gene : {m_gene}')
                # print(f'{self.generation} generation \
                #     max score : {m_score}')



genetic_algo = Genetic(10, 40)
score = 0
# genetic_algo.generate()
# for _ in range(10):
#     genetic_algo.generate(cross_p=0.8, mutation_p=0.05)

genetic_algo.generate_ntimes(20000, cross_p=0.5, mutation_p=0.2, print_several_times=1000)





"""

import random
random.seed(10)

def cal_fitness(queens):
    l = len(queens)
    fit_cnt = 0
    for i in range(l):
        for j in range(i+1, l):
            x_i, y_i = queens[i]
            x_j, y_j = queens[j]
            if x_i!=x_j and y_i!=y_j and abs((y_i-y_j)/(x_i-x_j))!=1:
                fit_cnt += 1     
    return fit_cnt

def is_solution(max_score, board_size):
    solution_num = (board_size*(board_size-1))//2
    if max_score==solution_num:
        return True
    else:
        return False
    

class Genetic:
    def __init__(self, board_size, gene_num):
        self.generation = 1
        self.board_size = board_size
        self.gene_num = gene_num
        self.genes = [[(i, random.randrange(1, board_size+1)) for i in range(1, board_size+1)] \
                     for _ in range(gene_num)]
        
    def selection(self):
        scores = list(map(cal_fitness, self.genes))
        m_score = max(scores)
        m_idx = scores.index(m_score)
        m_gene = self.genes[m_idx]
        self.genes = random.choices(self.genes, weights=scores, k=self.gene_num)
        return scores, m_gene
        
    def crossover(self, p=0.5):
        p = p/2
        n = int(self.gene_num*p)
        pick_nums = random.sample(range(self.gene_num), k=n*2)
        for i in range(n):
            cross_point = random.randrange(1, self.board_size)
            
            idx1 = pick_nums[i*2]
            idx2 = pick_nums[i*2+1]
                             
            tar1 = [y for x, y in self.genes[idx1]]
            tar2 = [y for x, y in self.genes[idx2]]
            new_tar1 = tar1[:cross_point] + tar2[cross_point:]
            new_tar2 = tar1[cross_point:] + tar2[:cross_point]
            self.genes[idx1] = [(x, y) for x, y in enumerate(new_tar1, start=1)]
            self.genes[idx2] = [(x, y) for x, y in enumerate(new_tar2, start=1)]
            
    def mutation(self, theta=0.5):
        for gene_idx in range(self.gene_num):
            for info_idx in range(self.board_size):
                if random.random()<theta:
                    mut_num = random.randrange(1, self.board_size+1)
                    self.genes[gene_idx][info_idx] = (info_idx+1, mut_num)
    

    def generate(self, cross_p=0.5, mutation_p=0.5):
        scores, m_gene = self.selection()
        self.crossover(p=cross_p)
        self.mutation(theta=mutation_p)
        self.generation += 1
        return max(scores), m_gene


    def generate_ntimes(self, iteration, cross_p=0.5, mutation_p=0.5, print_several_times=100):
        for i in range(iteration):
            m_score, m_gene = self.generate(cross_p, mutation_p)
            if is_solution(m_score, self.board_size):
                print(f"{i} generation's solotion : {m_gene}")
            if self.generation%print_several_times==0:
                print(f'{self.generation} generation \
                    max score : {m_score}, gene : {m_gene}')
                # print(f'{self.generation} generation \
                #     max score : {m_score}')



genetic_algo = Genetic(10, 40)
score = 0
# genetic_algo.generate()
# for _ in range(10):
#     genetic_algo.generate(cross_p=0.8, mutation_p=0.05)

genetic_algo.generate_ntimes(20000, cross_p=0.5, mutation_p=0.2, print_several_times=1000)


'''
성능이 오르지 않는다.
의문1 : 교차가 임의로 저렇게 일어나는 것이 맞는가?

'''"""