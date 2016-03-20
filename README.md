toppit
======
My name is Tyler, and I'm a cat-gif-aholic. toppit pulls top posts from user specified subreddits and emails them to 
the user so we don't spend too much time looking at garbage. 

Configuration
-------------
toppit is mostly all configurable

    - Sender
    - Recipients
    - Subreddits
    - Interval
    - Post Counts
    
are configurable using the `.toppit` configuration file.

Below is an example `.toppit` configuration file. This configuration will email `top 5 posts` of the `day` from the `programming`
and `headphones` subreddits to `me@gmail.com`

```
[toppit]

Email: me@gmail.com
Password: secret_password
Recipients: me@gmail.com
Subreddits: programming,headphones
Interval: DAY
Count: 5
```