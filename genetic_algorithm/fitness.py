"""
Fitness Evaluation Module
Evaluates the quality of feature subsets
Developed by: Student 2
"""

import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier


class FitnessEvaluator:
    """
    FitnessEvaluator class for calculating chromosome fitness
    Fitness is based on classification accuracy and feature count
    """
    
    def __init__(self, X, y, model_type='random_forest', alpha=0.9, cv_folds=3):
        """
        Initialize the FitnessEvaluator
        
        Args:
            X: Feature matrix (samples x features)
            y: Target vector
            model_type: ML model to use ('random_forest', 'svm', 'knn')
            alpha: Weight for accuracy (1-alpha for feature reduction)
                  Higher alpha = prioritize accuracy
                  Lower alpha = prioritize fewer features
            cv_folds: Number of cross-validation folds
        """
        self.X = X
        self.y = y
        self.model_type = model_type
        self.alpha = alpha
        self.cv_folds = cv_folds
        self.n_features = X.shape[1]
        
        # Initialize ML model
        self.model = self._create_model()
        
        # Track evaluations
        self.evaluation_count = 0
    
    def _create_model(self):
        """
        Create ML model based on model_type
        
        Returns:
            Scikit-learn classifier
        """
        if self.model_type == 'random_forest':
            return RandomForestClassifier(
                n_estimators=50, 
                max_depth=10,
                random_state=42,
                n_jobs=-1
            )
        elif self.model_type == 'svm':
            return SVC(
                kernel='rbf',
                random_state=42
            )
        elif self.model_type == 'knn':
            return KNeighborsClassifier(
                n_neighbors=5,
                n_jobs=-1
            )
        else:
            raise ValueError(f"Unknown model type: {self.model_type}")
    
    def evaluate_chromosome(self, chromosome):
        """
        Evaluate fitness of a chromosome
        
        Args:
            chromosome: Chromosome object to evaluate
            
        Returns:
            float: Fitness score (0 to 1, higher is better)
        """
        # Get selected features
        selected_features = chromosome.get_selected_features()
        n_selected = len(selected_features)
        
        # Check if any features are selected
        if n_selected == 0:
            chromosome.fitness = 0.0
            chromosome.accuracy = 0.0
            return 0.0
        
        # Extract selected features from dataset
        X_selected = self.X[:, selected_features]
        
        # Evaluate model performance using cross-validation
        try:
            cv_scores = cross_val_score(
                self.model, 
                X_selected, 
                self.y,
                cv=self.cv_folds,
                scoring='accuracy',
                n_jobs=-1
            )
            accuracy = np.mean(cv_scores)
        except Exception as e:
            print(f"Error during cross-validation: {str(e)}")
            accuracy = 0.0
        
        # Calculate feature reduction ratio
        feature_ratio = 1.0 - (n_selected / self.n_features)
        
        # Calculate fitness (weighted sum of accuracy and feature reduction)
        fitness = (self.alpha * accuracy) + ((1 - self.alpha) * feature_ratio)
        
        # Update chromosome
        chromosome.fitness = fitness
        chromosome.accuracy = accuracy
        
        # Increment evaluation counter
        self.evaluation_count += 1
        
        return fitness
    
    def evaluate_population(self, population):
        """
        Evaluate fitness for entire population
        
        Args:
            population: List of Chromosome objects
            
        Returns:
            numpy array of fitness scores
        """
        fitness_scores = []
        
        for chromosome in population:
            fitness = self.evaluate_chromosome(chromosome)
            fitness_scores.append(fitness)
        
        return np.array(fitness_scores)
    
    def get_best_chromosome(self, population):
        """
        Find chromosome with highest fitness in population
        
        Args:
            population: List of Chromosome objects
            
        Returns:
            Chromosome with highest fitness
        """
        return max(population, key=lambda c: c.fitness)
    
    def get_worst_chromosome(self, population):
        """
        Find chromosome with lowest fitness in population
        
        Args:
            population: List of Chromosome objects
            
        Returns:
            Chromosome with lowest fitness
        """
        return min(population, key=lambda c: c.fitness)
    
    def get_average_fitness(self, population):
        """
        Calculate average fitness of population
        
        Args:
            population: List of Chromosome objects
            
        Returns:
            float: Average fitness
        """
        return np.mean([c.fitness for c in population])
    
    def get_population_stats(self, population):
        """
        Get statistics about population fitness
        
        Args:
            population: List of Chromosome objects
            
        Returns:
            dict: Statistics (best, worst, average, std)
        """
        fitness_values = [c.fitness for c in population]
        
        return {
            'best_fitness': np.max(fitness_values),
            'worst_fitness': np.min(fitness_values),
            'avg_fitness': np.mean(fitness_values),
            'std_fitness': np.std(fitness_values),
            'best_accuracy': max([c.accuracy for c in population]),
            'avg_features': np.mean([c.n_selected_features for c in population])
        }
    
    def evaluate_feature_subset(self, feature_indices):
        """
        Directly evaluate a feature subset (helper method)
        
        Args:
            feature_indices: Array of feature indices
            
        Returns:
            float: Accuracy score
        """
        if len(feature_indices) == 0:
            return 0.0
        
        X_selected = self.X[:, feature_indices]
        
        try:
            cv_scores = cross_val_score(
                self.model,
                X_selected,
                self.y,
                cv=self.cv_folds,
                scoring='accuracy',
                n_jobs=-1
            )
            accuracy = np.mean(cv_scores)
        except:
            accuracy = 0.0
        
        return accuracy


# Example usage
if __name__ == '__main__':
    from chromosome import Chromosome
    from sklearn.datasets import load_iris
    
    print("="*60)
    print("FITNESS EVALUATOR EXAMPLE")
    print("="*60)
    
    # Load sample data
    X, y = load_iris(return_X_y=True)
    print(f"\nDataset: {X.shape[0]} samples, {X.shape[1]} features")
    
    # Create fitness evaluator
    evaluator = FitnessEvaluator(X, y, model_type='random_forest', alpha=0.9)
    
    # Create a chromosome
    chromosome = Chromosome(n_features=X.shape[1])
    print(f"\nChromosome: {chromosome.genes}")
    print(f"Selected features: {chromosome.get_selected_features()}")
    
    # Evaluate fitness
    fitness = evaluator.evaluate_chromosome(chromosome)
    print(f"\nFitness: {fitness:.4f}")
    print(f"Accuracy: {chromosome.accuracy:.4f}")
    print(f"Selected features: {chromosome.n_selected_features}/{X.shape[1]}")
    
    # Create and evaluate population
    print("\n" + "="*60)
    print("POPULATION EVALUATION")
    print("="*60)
    
    population = Chromosome.create_random_population(10, X.shape[1])
    evaluator.evaluate_population(population)
    
    stats = evaluator.get_population_stats(population)
    print(f"\nPopulation Statistics:")
    print(f"  Best Fitness: {stats['best_fitness']:.4f}")
    print(f"  Worst Fitness: {stats['worst_fitness']:.4f}")
    print(f"  Average Fitness: {stats['avg_fitness']:.4f}")
    print(f"  Best Accuracy: {stats['best_accuracy']:.4f}")
    print(f"  Avg Features: {stats['avg_features']:.1f}")
    
    # Get best chromosome
    best = evaluator.get_best_chromosome(population)
    print(f"\nBest Chromosome:")
    print(f"  {best}")

