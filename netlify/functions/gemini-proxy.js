// Netlify Function: Gemini API proxy
//
// Keeps the Gemini API key server-side. The browser calls
// /api/gemini (redirected to this function via netlify.toml) instead of
// calling generativelanguage.googleapis.com directly with an embedded key.
//
// Set GEMINI_API_KEY in Netlify: Site settings → Environment variables.

const GEMINI_MODEL = 'gemini-2.5-flash';

exports.handler = async (event) => {
  const corsHeaders = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
  };

  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 200, headers: corsHeaders, body: '' };
  }

  if (event.httpMethod !== 'POST') {
    return {
      statusCode: 405,
      headers: corsHeaders,
      body: JSON.stringify({ error: { message: 'Method not allowed' } }),
    };
  }

  const apiKey = process.env.GEMINI_API_KEY;
  if (!apiKey) {
    return {
      statusCode: 500,
      headers: corsHeaders,
      body: JSON.stringify({ error: { message: 'Server misconfigured: GEMINI_API_KEY is not set' } }),
    };
  }

  try {
    const upstream = await fetch(
      `https://generativelanguage.googleapis.com/v1beta/models/${GEMINI_MODEL}:generateContent?key=${apiKey}`,
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: event.body,
      }
    );

    const data = await upstream.text();

    return {
      statusCode: upstream.status,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      body: data,
    };
  } catch (err) {
    return {
      statusCode: 502,
      headers: corsHeaders,
      body: JSON.stringify({ error: { message: 'Failed to reach Gemini API: ' + err.message } }),
    };
  }
};
