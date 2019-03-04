About

Trace-cmd tests according to the CI wiki specifically the standard test interface in the [spec](https://fedoraproject.org/wiki/Changes/InvokingTests).

The playbook includes Tier1 level test cases that have been tested in classic contexts and is passing reliably.

The following steps are used to execute the tests using the standard test interface:

Test environment

Make sure you have installed packages from the spec

    `# dnf install ansible python2-dnf libselinux-python standard-test-roles ansible python2-dnf libselinux-python standard-test-roles`

Run tests for Classic
~~~~
    # export TEST_SUBJECTS=
    # sudo ansible-playbook --tags=classic tests.yml
~~~~

Snip of the example test run for Classic tests:

> TASK [standard-test-beakerlib : Run beakerlib tests] *****************************************************************************************************************************************
>
> changed: [localhost] => (item=sanity)
> 
> TASK [standard-test-beakerlib : Make the master tests summary log artifact] ******************************************************************************************************************
>
> changed: [localhost] => (item=sanity)
> 
> TASK [standard-test-beakerlib : Check the results] *******************************************************************************************************************************************
>
> changed: [localhost]
> 
> TASK [standard-test-beakerlib : include_role] ************************************************************************************************************************************************
> 
> TASK [str-common : Pull out the logs from test environment to test runner] *******************************************************************************************************************
>
> changed: [localhost]
> 
> PLAY RECAP ***********************************************************************************************************************************************************************************
> 
> localhost                  : ok=27   changed=16   unreachable=0    failed=0   
> 
