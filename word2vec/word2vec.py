# first we need to define our embeddings matrix
# we define the matrix according to the len of unique words we have
# at the beginning the matrix has random variables from -1 to 1
# we also define the embeddings size which is the size of the vectors representing 
# the vectors
embeddings = tf.Variable(tf.random_uniform([vocabulary_size, embedding_size], -1.0, 1.0))
# the noise-contrastive estimation loss is defined in terms of logisitic regression model
# therefore we need to define the weights and biases for each word in the vocabulary
# 
nce_weights = tf.Variable(tf.truncated_normal([vocabulary_size, embedding_size],stddev=1.0 / math.sqrt(embedding_size)))
nce_biases = tf.Variable(tf.zeros([vocabulary_size]))



#placeholders for the inputs
train_inputs = tf.placeholder(tf.int32, shape=[batch_size])
train_labels = tf.placeholder(tf.int32, shape=[batch_size, 1])

embed = tf.nn.embedding_lookup(embeddings, train_inputs)

