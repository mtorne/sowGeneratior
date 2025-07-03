const express = require('express');
const bodyParser = require('body-parser');
const { DefaultRequestSigner } = require('oci-common');
const https = require('https');

const app = express();
const port = 3000;

app.use(bodyParser.json());
app.use(express.static('public'));

app.post('/api/chat', async (req, res) => {
    const prompt = req.body.prompt;

    const signer = new DefaultRequestSigner();
    const requestBody = JSON.stringify({
        compartmentId: '<your_compartment_ocid>',
        modelId: 'cohere.command',
        prompt: prompt,
        maxTokens: 100
    });

    const options = {
        hostname: 'generativeai.aiservice.<region>.oci.oraclecloud.com',
        path: '/20231130/actions/generateText',
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Content-Length': Buffer.byteLength(requestBody),
            'opc-request-id': `req-${Date.now()}`
        }
    };

    signer.signRequest(options, requestBody);

    const reqAI = https.request(options, (ociRes) => {
        let data = '';
        ociRes.on('data', chunk => data += chunk);
        ociRes.on('end', () => {
            try {
                const parsed = JSON.parse(data);
                res.json({ reply: parsed.generatedText || 'No reply' });
            } catch (e) {
                res.status(500).json({ error: 'Invalid response from OCI API' });
            }
        });
    });

    reqAI.on('error', (e) => res.status(500).send(`Error: ${e.message}`));
    reqAI.write(requestBody);
    reqAI.end();
});

app.listen(port, () => {
    console.log(`✅ Server running at http://localhost:${port}`);
});
