# DEDUPE
##### by [Chandra S S Vamsi](https://in.linkedin.com/in/ucssv)


### Configuration
- Install Django, Dedupe and other dependencies in a virtual-env.

  ```
  pip install django
  pip install dedupe
  ```
  
- Clone the repo.
- Start **Apache** and **MySQL** on _localhost_.
- In **_dedupe/settings.py_** set your database name, username and password. Head over to your _localhost/phpmyadmin_ and create a new database with the same name.
- Make migrations and run the server as:

  ```
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
  ```
  
### Usage
  **_Caution_**: Refrain from refreshing page in between the process of _deduping_ to avoid data loss.
- Upload your _data file_, give a name to it and Submit.
- Select the _Unique Identity Column_ of your data-set and the _Columns_ based on which the data is supposed to be deduped.
- Train the system

  | Option   | Result   |
  | :--------: | :--------: |
  | Yes      | The machine treats all similar data pairs to be the same  |
  | No       | The machine treats all similar data pairs to be different |
  | Unsure   | The machine skips that question from training             |
  | Finish   | The machine stops training and starts deduping the data.  |
  
- Wait till the system redirects you to a page with an option to download the output file. Then download the file by clicking on it.
- The output file consists of two new columns added in the front namely **_Cluster ID_** and **_Confidence Score_**. The Cluster ID is same for all the data rows belonging to the same Cluster.
- **_Tip_** : Sort the Confidence Score in descending order and Cluster ID to estimate the accuracy of the Deduping.

### Acknowledgement
- Thanks to my team-mates **_Aarti Barai_** and **_Piyush Agarwal_**.
- Thanks to **_Lakshya Foundation_** and **_Innovation Garage_** for providng us an awesome platform **_Makeathon - 6.0_**  to showcase our skills.
- Thanks to **_Almabse_** for providing the challenging Problem Statement and to our mentors **_Kalyan Verma_** and **_Vaibhav Awachat_**.

### Contact
   Drop a mail at _ucssvamsi@gmail.com_

