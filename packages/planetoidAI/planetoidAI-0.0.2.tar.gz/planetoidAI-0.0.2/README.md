# Planetoid API

 Planetoid's API official library to access free APIs
 
 <div id="top"></div>

[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://planetoid.pythonanywhere.com/">
    <img src="https://planetoid.pythonanywhere.com/static/5ebd9c17efef0e2515e12933_Logo-Planetoid-New.png" alt="Planetoid logo" hight="600">
  </a>

</div>


<!-- ABOUT THE PROJECT -->
## About The API

Planetoid's official library to access free APIs!

<a href="https://planetoid.pythonanywhere.com/"><strong>Explore more »</strong></a>

### Built With

<!-- This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples. -->

* [Core python](https://www.python.org/)
<!-- * [JQuery](https://jquery.com) -->
<!-- <p align="right">(<a href="#top">back to top</a>)</p> -->

<!-- GETTING STARTED -->
## Getting Started

<!-- This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.
 -->
### Prerequisites
<!-- This is an example of how to list things you need to use the software and how to install them. -->
* Python 3 

### Installation

<!-- _Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._ -->
<!-- 
1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ``` -->
1. Install pip package
 
   ```sh
   pip install planetoidAI
   
   ```
<!-- 4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```
 -->
<!-- <p align="right">(<a href="#top">back to top</a>)</p> -->

<!-- USAGE EXAMPLES -->
## Usage 

Useful examples of how a project can be used. 

Create a new python file anywhere, such as demo.py.
Add code in the demo.py file, the sample code is as follows:

## 1. Object detection
```python

from planetoidAI import Planetoid

planetoid1 = Planetoid()

# Get_objects_from_image

object_list = planetoid1.get_objects_from_image("FILENAME.jpg")

print(object_list)

```
### OUTPUT

```javascript
[{
'name': 'Object', 
'class_name': 'person', 
'score': 0.5407423377037048, 
'y': 0.215625, 'x': 0.090625, 'height': 0.984375, 'width': 0.896875
}]
```

## 2. Get face location from image
```python

from planetoidAI import Planetoid

planetoid1 = Planetoid()

# Get_face_location_from_image
face_276 = planetoid1.get_face_location_from_image( filename= "FILENAME.jpeg")
print(face_276)

```
### OUTPUT

```javascript
[{
'name': 'Object', 
'class_name': 'face', 
'score': 0.9999943971633911, 
'y': 0.30875, 'x': 0.32625, 'height': 0.65375, 'width': 0.67125
}]
```


## 3. Age and gender recognition
```python

from planetoidAI import Planetoid

planetoid1 = Planetoid()

# Get_age_gender_from_image
age_gender = planetoid1.get_age_gender_from_image("FILENAME.jpeg")
print(age_gender)


```
### OUTPUT

```javascript
[{
'name': 'Object', 
'class_name': 'male, 
Age: (15-17)', 
'score': 0.4520128, 
'y': 0.30875, 'x': 0.32625, 'height': 0.65375, 'width': 0.67125
}]
```

## 4. Nationality recognition (Face race)
```python

from planetoidAI import Planetoid

planetoid1 = Planetoid()

# Get_face_race_from_image
nationality = planetoid1.get_face_race_from_image("FILEMNAME.jpeg")
print(nationality)


```
### OUTPUT

```javascript
[{
'name': 'Object', 
'class_name': 'Indian', 
'score': 0.97603726, 
'y': 0.30875, 'x': 0.32625, 'height': 0.65375, 'width': 0.67125
}]

```

## 5. Language translation
```python

from planetoidAI import Planetoid

planetoid1 = Planetoid()

# Get_translation
translation = planetoid1.get_translation("hello", translate_to='gu')
print(translation)

```
### OUTPUT

```javascript

{'translation': 'નમસ્તે'}

```

<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- CONTACT -->
## Contact

Himanshu Molya 

Project Link: [https://github.com/HimanshuMoliya/planetoid](https://github.com/HimanshuMoliya/planetoid)

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [GitHub Pages](https://pages.github.com)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- [contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors -->
[forks-shield]: https://img.shields.io/github/forks/HimanshuMoliya/planetoid.svg?style=for-the-badge
[forks-url]: https://github.com/HimanshuMoliya/planetoid/network/members
[stars-shield]: https://img.shields.io/github/stars/HimanshuMoliya/planetoid.svg?style=for-the-badge
[stars-url]: https://github.com/HimanshuMoliya/planetoid/stargazers
[issues-shield]: https://img.shields.io/github/issues/HimanshuMoliya/planetoid.svg?style=for-the-badge
[issues-url]: https://github.com/HimanshuMoliya/planetoid/issues
[license-shield]: https://img.shields.io/github/license/HimanshuMoliya/planetoid.svg?style=for-the-badge
[license-url]: https://github.com/HimanshuMoliya/planetoid/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/company/planetoid/
[product-screenshot]: images/screenshot.png
