def abstract():
    import inspect
    caller = inspect.getouterframes(inspect.currentframe())[1][3]
    raise NotImplementedError(caller + ' must be implemented in subclass')

class Aggregator(object):
    
    def __init__(self, domain_labels, directed = False):
        self.domain_labels = domain_labels # The list of labels in the domain
        self.directed = directed # Whether we should use edge directions for creating the aggregation
    
    def aggregate(self, graph, node, conditional_node_to_label_map):
        ''' Given a node, its graph, and labels to condition on (observed and/or predicted)
        create and return a feature vector for neighbors of this node.
        If a neighbor is not in conditional_node_to_label_map, ignore it.
        If directed = True, create and append two feature vectors;
        one for the out-neighbors and one for the in-neighbors.
        '''
        abstract()

class CountAggregator(Aggregator):
    '''The count aggregate'''

    def aggregate(self, graph, node, conditional_node_to_label_map): 
        if not self.directed:

           neighbors=graph.get_neighbors(node)

           l=[]
           labels=[]
           labelset=[]
           for i in neighbors:
               l=conditional_node_to_label_map.get(i)
               if l in self.domain_labels:
                  labelset.append(l)
           for i in self.domain_labels:
                c=[]
                c.append(float(labelset.count(i)))
                for i in c:     
                    labels.append(float(i))
           FV2=labels
           
        else:
           InNeighbors=graph.get_in_neighbors(node)                   
           Inl=[]
           Inlabels=[]
           Inlabelset=[]

           for i in InNeighbors:
               Inl=conditional_node_to_label_map.get(i)
               if Inl in self.domain_labels:
                  Inlabelset.append(Inl)
           for i in self.domain_labels:
                c=[]
                c.append(float(Inlabelset.count(i)))
                for i in c:     
                    Inlabels.append(float(i))
           FvIN=Inlabels

           OutNeighbors=graph.get_out_neighbors(node)
           Outl=[]
           Outlabels=[]
           Outlabelset=[]

           for i in OutNeighbors:
               Outl=conditional_node_to_label_map.get(i)
               if Outl in self.domain_labels:
                  Outlabelset.append(Outl)
           for i in self.domain_labels:
                c=[]
                c.append(float(Outlabelset.count(i)))
                for i in c:     
                    Outlabels.append(float(i))
           FvOut=Outlabels
          
           FV2 = FvIN + FvOut
        return FV2


class ProportionalAggregator(Aggregator):
    '''The proportional aggregate'''
    
    def aggregate(self, graph, node, conditional_node_to_label_map): 
        if not self.directed:
#Neighbors Calculation Undirected:       
           neighbors=graph.get_neighbors(node)

           l=[]
           labels=[]
           labelset=[]
           c=[]
           for i in neighbors:
               l=conditional_node_to_label_map.get(i)
               if l in self.domain_labels:
                  labelset.append(l)
           if not len(labelset)==0:
              for i in self.domain_labels:
                  if i in labelset:
                     c.append(float(labelset.count(i))/float(len(labelset)))
                  else:
                     c.append(0.0)
           else:
             for i in self.domain_labels:
                  c.append(0.0)    
           
           FV2=c
           
        else:
#Directed In Neighbors Calculation
           InNeighbors=graph.get_in_neighbors(node)                   
           
           Inl=[]
           Inlabels=[]
           Inlabelset=[]
           for i in InNeighbors:
               Inl=conditional_node_to_label_map.get(i)
               if Inl in self.domain_labels:
                  Inlabelset.append(Inl)
           if not len(Inlabelset)==0:
              for i in self.domain_labels:
                  if i in Inlabelset:
                     Inlabels.append(float(Inlabelset.count(i))/float(len(Inlabelset)))
                  else:
                     Inlabels.append(0.0)
           else:
             for i in self.domain_labels:
                  Inlabels.append(0.0)    
          
           FvIN=Inlabels
           
#Directed Out Neighbors Calculation
           OutNeighbors=graph.get_out_neighbors(node)
           Outl=[]
           Outlabels=[]
           Outlabelset=[]
           for i in OutNeighbors:
               Outl=conditional_node_to_label_map.get(i)
               if Outl in self.domain_labels:
                  Outlabelset.append(Outl)
           if not len(Outlabelset)==0:
              for i in self.domain_labels:
                  if i in Outlabelset:
                     Outlabels.append(float(Outlabelset.count(i))/float(len(Outlabelset)))
                  else:
                     Outlabels.append(0.0)
           else:
             for i in self.domain_labels:
                  Outlabels.append(0.0)    
          
           FvOut=Outlabels
          
           FV2 = FvIN + FvOut
        return FV2


class ExistAggregator(Aggregator):
    '''The exist aggregate'''
    
    def aggregate(self, graph, node, conditional_node_to_label_map): 
        if not self.directed:
           
           neighbors=graph.get_neighbors(node)
           l=[]
           labels=[]
           labelset=[]
           for i in neighbors:
               l=conditional_node_to_label_map.get(i)
               if l in self.domain_labels:
                  labelset.append(l)
           for i in self.domain_labels:
                if i in labelset:
                   c=1.0
                else:
                   c=0.0
                labels.append(c)
           FV2=labels
           
        else:
           InNeighbors=graph.get_in_neighbors(node)                   
           Inl=[]
           Inlabels=[]
           Inlabelset=[]

           for i in InNeighbors:
               Inl=conditional_node_to_label_map.get(i)
               if Inl in self.domain_labels:
                  Inlabelset.append(Inl)
           for i in self.domain_labels:
                if i in Inlabelset:
                   c=1.0
                else:
                   c=0.0
                Inlabels.append(c)
           FvIN=Inlabels

           OutNeighbors=graph.get_out_neighbors(node)
           Outl=[]
           Outlabels=[]
           Outlabelset=[]

           for i in OutNeighbors:
               Outl=conditional_node_to_label_map.get(i)
               if Outl in self.domain_labels:
                  Outlabelset.append(Outl)
           for i in self.domain_labels:
                if i in Outlabelset:
                   c=1.0
                else:
                   c=0.0
                Outlabels.append(c)
           FvOut=Outlabels
          
           FV2 = FvIN + FvOut
        return FV2
        #raise NotImplementedError('You need to implement this method')


def get_class( kls ):
    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = __import__( module )
    for comp in parts[1:]:
        m = getattr(m, comp)
    return m

class Classifier(object):


    def __init__(self, scikit_classifier_name, **classifier_args):        
        classifer_class=get_class(scikit_classifier_name)
        self.clf = classifer_class(**classifier_args)

    
    def fit(self, graph, train_indices):
        abstract()
    
    def predict(self, graph, test_indices, conditional_node_to_label_map = None):
        abstract()

class LocalClassifier(Classifier):

    def fit(self, graph, train_indices):

        X=[graph.node_list[t].feature_vector for t in train_indices]     
        
        Y=[graph.node_list[t].label for t in train_indices]
        self.clf.fit(X,Y)

    def predict(self, graph, test_indices, conditional_node_to_label_map = None):

        X=[graph.node_list[t].feature_vector for t in test_indices]
        
        return self.clf.predict(X)

class RelationalClassifier(Classifier):
    
    def __init__(self, scikit_classifier_name, aggregator, use_node_attributes = False,directed = False, **classifier_args):
        super(RelationalClassifier, self).__init__(scikit_classifier_name, **classifier_args)
        self.aggregator = aggregator
        self.use_node_attributes = use_node_attributes
        self.directed=directed

    def NeighborsUpdate(self,graph,node,test_indices,conditional_node_to_label_map):
        if self.use_node_attributes==True:   
           if not self.directed:
              neighbors=graph.get_neighbors(node)
              for i in neighbors:
                for t in test_indices:
                   if i==graph.node_list[t]:
                      FV1 = graph.node_list[t].feature_vector                
                      FV2 = self.aggregator.aggregate(graph,graph.node_list[t],conditional_node_to_label_map)
                      x=FV1 + FV2
                      label=self.clf.predict(x)
                      if conditional_node_to_label_map[graph.node_list[t]]== 'None' or conditional_node_to_label_map[graph.node_list[t]]!=label:
                         conditional_node_to_label_map[graph.node_list[t]]=label
                         node=graph.node_list[t]
                         self.NeighborsUpdate(graph,node,test_indices,conditional_node_to_label_map)
           else:
              InNeighbors=graph.get_in_neighbors(node)
              for i in InNeighbors:
                  for t in test_indices:
                      if i==graph.node_list[t]:
                         FV1 = graph.node_list[t].feature_vector                
                         FV2 = self.aggregator.aggregate(graph,graph.node_list[t],conditional_node_to_label_map)
                         x=FV1 + FV2
                         label=self.clf.predict(x)
                         if conditional_node_to_label_map[graph.node_list[t]]== 'None' or conditional_node_to_label_map[graph.node_list[t]]!=label:
                            conditional_node_to_label_map[graph.node_list[t]]=label
                            node=graph.node_list[t]
                            self.NeighborsUpdate(graph,node,test_indices,conditional_node_to_label_map)

              OutNeighbors=graph.get_out_neighbors(node)
              for i in OutNeighbors:
                  for t in test_indices:
                      if i==graph.node_list[t]:
                         FV1 = graph.node_list[t].feature_vector                
                         FV2 = self.aggregator.aggregate(graph,graph.node_list[t],conditional_node_to_label_map)
                         x=FV1 + FV2
                         label=self.clf.predict(x)
                         if conditional_node_to_label_map[graph.node_list[t]]== 'None' or conditional_node_to_label_map[graph.node_list[t]]!=label:
                            conditional_node_to_label_map[graph.node_list[t]]=label
                            node=graph.node_list[t]
                            self.NeighborsUpdate(graph,node,test_indices,conditional_node_to_label_map)
        else:
           if not self.directed:
              neighbors=graph.get_neighbors(node)
              for i in neighbors:
                for t in test_indices:
                   if i==graph.node_list[t]:
                     
                      FV2 = self.aggregator.aggregate(graph,graph.node_list[t],conditional_node_to_label_map)
                      x=FV2
                      label=self.clf.predict(x)
                      if conditional_node_to_label_map[graph.node_list[t]]== 'None' or conditional_node_to_label_map[graph.node_list[t]]!=label:
                         conditional_node_to_label_map[graph.node_list[t]]=label
                         node=graph.node_list[t]
                         self.NeighborsUpdate(graph,node,test_indices,conditional_node_to_label_map)
           else:
              InNeighbors=graph.get_in_neighbors(node)
              for i in InNeighbors:
                  for t in test_indices:
                      if i==graph.node_list[t]:
                      
                         FV2 = self.aggregator.aggregate(graph,graph.node_list[t],conditional_node_to_label_map)
                         x=FV2
                         label=self.clf.predict(x)
                         if conditional_node_to_label_map[graph.node_list[t]]== 'None' or conditional_node_to_label_map[graph.node_list[t]]!=label:
                            conditional_node_to_label_map[graph.node_list[t]]=label
                            node=graph.node_list[t]
                            self.NeighborsUpdate(graph,node,test_indices,conditional_node_to_label_map)

              OutNeighbors=graph.get_out_neighbors(node)
              for i in OutNeighbors:
                  for t in test_indices:
                      if i==graph.node_list[t]:
                        
                         FV2 = self.aggregator.aggregate(graph,graph.node_list[t],conditional_node_to_label_map)
                         x=FV2
                         label=self.clf.predict(x)
                         if conditional_node_to_label_map[graph.node_list[t]]== 'None' or conditional_node_to_label_map[graph.node_list[t]]!=label:
                            conditional_node_to_label_map[graph.node_list[t]]=label
                            node=graph.node_list[t]
                            self.NeighborsUpdate(graph,node,test_indices,conditional_node_to_label_map)
            
    
        return conditional_node_to_label_map

    def fit(self, graph, train_indices):

        conditional_map={}
        X=[]
        for t in train_indices:
           conditional_map[graph.node_list[t]]=graph.node_list[t].label
        
        for t in train_indices:
            if self.use_node_attributes==True:
               FV1 = graph.node_list[t].feature_vector                
               FV2 = self.aggregator.aggregate(graph,graph.node_list[t],conditional_map)
               x=FV1 + FV2

            else:
               x= self.aggregator.aggregate(graph,graph.node_list[t],conditional_map)
               
            X.append(x)
       
        Y=[graph.node_list[t].label for t in train_indices]
                  
        self.clf.fit(X,Y)
        
          
    def predict(self, graph, test_indices, conditional_node_to_label_map = None):
    
        X=[]
        for t in test_indices:
            if self.use_node_attributes==True:
#Node Feature values
               FV1 = graph.node_list[t].feature_vector                
#Neighbors Aggregated Feature
               FV2 = self.aggregator.aggregate(graph,graph.node_list[t],conditional_node_to_label_map)
               x=FV1 + FV2
               label=self.clf.predict(x)
#Add predicted label of Test node
               if conditional_node_to_label_map[graph.node_list[t]]== 'None' or conditional_node_to_label_map[graph.node_list[t]]!=label:
                  conditional_node_to_label_map[graph.node_list[t]]=label
                  node=graph.node_list[t]
                  self.NeighborsUpdate(graph,node,test_indices,conditional_node_to_label_map)

               if label==conditional_node_to_label_map[graph.node_list[t]]:
                  X.append(label)
               else:
                  X.append(conditional_node_to_label_map[graph.node_list[t]])

            else:
#Neighbors Aggregated Feature without Node values
               x= self.aggregator.aggregate(graph,graph.node_list[t],conditional_node_to_label_map)
#Predict the label
               label=self.clf.predict(x)
#Add predicted label of Test node
               if conditional_node_to_label_map[graph.node_list[t]]== 'None' or conditional_node_to_label_map[graph.node_list[t]]!=label:
                  conditional_node_to_label_map[graph.node_list[t]]=label
                  node=graph.node_list[t]
                  self.NeighborsUpdate(graph,node,test_indices,conditional_node_to_label_map)

               if label==conditional_node_to_label_map[graph.node_list[t]]:
                  X.append(label)
               else:
                  X.append(conditional_node_to_label_map[graph.node_list[t]])

        return X
        
    
     
                 

class ICA(Classifier):
    
    def __init__(self, local_classifier, relational_classifier, max_iteration = 10):
        self.local_classifier = local_classifier
        self.relational_classifier = relational_classifier
        self.max_iteration = 10
    
    def Predicted_Nodes_Update(self,graph,conditional_node_to_label_map,PredictedLabels,test_indices):
        for i in range(len(PredictedLabels)):
            conditional_node_to_label_map[graph.node_list[test_indices[i]]]=PredictedLabels[i]
            
    def fit(self, graph, train_indices):
        self.local_classifier.fit(graph, train_indices)
        self.relational_classifier.fit(graph, train_indices)
    
    def predict(self, graph, test_indices, conditional_node_to_label_map = None):
        
        PredictedLables_From_Local=self.local_classifier.predict(graph,test_indices)
#Update the Test Node and Predicted labels to the conditional_node_to_label_map                  
        self.Predicted_Nodes_Update(graph,conditional_node_to_label_map,PredictedLables_From_Local,test_indices)

        for _ in range(self.max_iteration):
            PredictedLables_From_Relational=self.relational_classifier.predict(graph,test_indices,conditional_node_to_label_map)
            
        return PredictedLables_From_Relational


    
