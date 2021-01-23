# whogoesthere
Find out who my linux box is talking to

# Work Flow

* Fork this repo to your own account.
* Locally create a branch for your issue,

        $ git checkout -b issue_XXXX
* If you have any python packages you depend on, add them 
to the `requires` list in `setup.py`.
* Your files go into `whogoesthere/src/whogoesthere` directory.
* Do you work, then push

        $ git push -u origin issue_XXXX
* When you're done, create a pull request from your local fork and `issue_XXXX` branch, to the main fork and branch `main`.


Enjoy!

# Running The Tests

do this

    $ ./run_tests.sh
