# Single Shot Face Identifier
This identifier only takes one facial image to Identifi Faces.(Does not need to be trained with severl images of the face.)

# Theory

<h>The model consists of : </h>
1. Deep CNN as a feature extractor. (effecient net b3.. could use higher version but crashed notbook with 16gb VRAM)
2. Classification part that takes inputs as facial features of two faces and tells if the faces are of same person or not.

# <h1>USAGE</h1>

# <h2> 1.Directly The model </h2>
<h3>Step 1. Get Model From the kaggle link at bottom</h3>
<h3>Step 2. Model is keras model. Imoprt model by : </h3>
<h4>from tensorflow import keras<br>
model = keras.models.load_model('File Location') </h4>
<h3>Step 3. Model takes 2 images (shape : 224,224,3) as input . Predict if two faces are same by : </h3>
<h4>inp1=np.array([Image1])<br>
 inp2=np.array([Image2])<br>
 pred=model.predict(x=[inp1,inp2])</h4>
<h3>Step 4. Model gives a list as an output. <br>The output on 0 index is probability of two inputs not being same.<br> The output on index 1 gives probability of two faces given in input being same. </h3>

<h2> 2.Library.. </h2>


# Link To datadet, model and notebook used to train and test the model.<br>
https://www.kaggle.com/abhinavrawat/face-recognition-mini-project<br>
https://www.kaggle.com/abhinavrawat/face-identification
  
