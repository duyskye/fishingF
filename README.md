# fishingF
# Installation
1.Clone the repository:

    git clone https://github.com/duyskye/fishingF.git
    
2.Navigate into the project directory:

    cd fishingF
    
3.Install dependencies:

    pip install -r requirements.txt

or

    py -m pip install -r requirements.txt
    
4.Prepare input files:

Get Bearer token with chrome console (F12)

    'Bearer '+ localStorage.getItem('fishAuth');

Create `accounts.json` with Bearer token.


Example `accounts.json`:

    [

      "Bearer .......",
  
      "Bearer ......."
  
    ]

# Usage
Run the bot

    py main.py
    
or

    python3 main.py
