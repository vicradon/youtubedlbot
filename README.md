# Youtube DL Bot

A set of bots that allow you to download YouTube videos using a link and a start and end

## Deployment

This project is designed to be deployed to a virtual machine running Linux. It uses Github actions to handle CI/CD and Ansible to handle configuration management.

### Run the Playbook to Provision Resources

Before running the script that provisions the needed resources, create an inventory.ini file in the ansible directory and follow the `inventory.sample.ini` to populate your `inventory.ini` file with the required values for your virtual machine.

With that done, run the command below to run the playbook script that provisions resources on the VM:

```
ansible-playbook -i ansible/inventory.ini ansible/playbook.yml
```
