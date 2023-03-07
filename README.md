# RSAvsCK

The goal of this project ot to provide a novel analysis of the semantic security of quantum ready algorithims.

I will acomplish this by training a a ML Algorithim (Naive Bayes) to classify a message as enrypted or not encrypted. 
This will be done for RSA and Crytal-Kyber encryption systems. A better randomized system will be more difficult for the ML
to predict, as the ML represents an attacker in this case. This effectively guages semantic security.

>Consider M0=attack and M1=don't attack. If the adversary can distinguish which message you are sending to your troops, 
they can optimize their strategy to defeat you.

For message creation I implement PKS#11. Follow these steps to use this in python.
1. Pip install
'''
pip install python-pkcs11
'''
2. Done

XHR Failed?

We may be on the wrong version of python
- Nope, 3.8 is in usr/lib/python3



Notes:
-------------------------------------------------
i; I Have made edit to 123 of kyber in kyber-py
ii; Currently RSA datastream is run in RSA_Gen and CK in CK-Gen within Kyber-PY




TODO:
--------------------------------------------------
1. Pretty print from both CSVs
2. Verify CSV to ARFF
3. Develop some tests and run
4. Bundle up nicely
