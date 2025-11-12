module.exports = async function (context, req) {
  const token = req.headers['x-ms-token-aad-access-token']; // or 'x-ms-token-aad-id-token'
  if (!token) {
    context.res = { status: 401, body: 'No token header found. Are you signed in?' };
    return;
  }
  context.res = { status: 200, body: token }; // raw text to paste into jwt.ms / jwt.io
};
