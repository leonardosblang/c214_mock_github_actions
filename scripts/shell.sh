ls
echo "Installing email"
sudo apt-get install mutt
echo "Sending email using linux default email" | mutt -s "Test Email" leonardo.sabra@ges.inatel.br
