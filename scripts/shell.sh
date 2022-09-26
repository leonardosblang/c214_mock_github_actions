ls
echo "Installing email"
sudo apt-get install mutt
sudo apt-get update
echo "Sending email using linux default email" | mutt -s "Test Email" leonardo.sabra@ges.inatel.br
