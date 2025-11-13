# pfpA

[![pfp](https://github.com/CEVIGS/pfpA/actions/workflows/pfp.yml/badge.svg)](https://github.com/CEVIGS/pfpA/actions/workflows/pfp.yml)

The CEVIGS pfp-automation tools allows you to automatically set your profile picture every day to counter the force of the default KEGS pfp.

This works by downloading the chrome browser and opening it every morning automatically on the github server.

# Set up

0. make a github account
1. Copy this repository (NOT FORK)
> [!NOTE]
> It is recommended to set the visibility to private

![](https://github.com/user-attachments/assets/6eeb5ec0-2bf8-4894-91b2-78c80e485677)

2. Go to settings

<img width="1243" height="881" alt="image" src="https://github.com/user-attachments/assets/fbe628ca-a562-4002-a1eb-ced407227914" />

3. goto secrets and variables/actions
<img width="1250" height="881" alt="image" src="https://github.com/user-attachments/assets/fd60f070-fefd-4303-8969-dc61fb206869" />

4. Click `new repository secret`
<img width="891" height="684" alt="image" src="https://github.com/user-attachments/assets/22812d48-91a5-45a7-b5d1-7b7bd4a992c8" />

5. Set it like so (`KEGSCRAPER_USERNAME` = your email without `@kegs.org.uk`. e.g. jdoe_a16)
<img width="939" height="514" alt="image" src="https://github.com/user-attachments/assets/6b82ebc2-9a2a-48f3-94cd-38e521c31517" />

6. Then click add secret

7. Click `new repository secret` again

8. Set the value `KEGSCRAPER_SECRET` to your KEGS email password. This is required for the script to be able to log in.

<img width="904" height="470" alt="image" src="https://github.com/user-attachments/assets/75445b1d-2239-42c8-9e5f-5c0f2ad546e2" />

9. Click add secret

10. it should now work. But to check, go to actions:
<img width="1272" height="831" alt="image" src="https://github.com/user-attachments/assets/548adaf1-dacb-497c-a0d9-172122be09a1" />

11. go to pfp

<img width="1275" height="831" alt="image" src="https://github.com/user-attachments/assets/16145e3d-00e1-4078-a5c0-73b29907153a" />

12. it should say it has a workflow dispatch trigger. Click run workflow/run workflow

<img width="942" height="519" alt="image" src="https://github.com/user-attachments/assets/92f4da2b-6ad1-40b8-8b25-40fba5011256" />

13. It will take about 3-5 minutes. When it's done, it should give a green checkmark as the status (you may need to reload the page)

14. To view logs as it is working ... TOOD


Put your pfp images in the `pfps/` directory and one will be randomly picked each day.

You can edit the main.py script if you want different logic for choosing a pfp.
