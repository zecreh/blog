# Claim Arbitrum tokens using the arb_claim.py script
Create the client:
```sh
import Replicate from "replicate";

const replicate = new Replicate({
  // get your token from https://replicate.com/account
  auth: process.env.REPLICATE_API_TOKEN,
});
```
