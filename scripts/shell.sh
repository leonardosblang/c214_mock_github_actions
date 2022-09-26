ls
cd test
echo "Installing email"
sudo apt-get install mailutils
echo "End of installating"
echo "Sending email using linux default email" | mail -s "subject: S107 - Leonardo Lang" leonardo.sabra@ges.inatel.br