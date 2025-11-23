/** @type {import('next').NextConfig} */
const nextConfig = {
  transpilePackages: ['@adk-course/shared'],
  async rewrites() {
    return [
      {
        source: '/api/agents/:path*',
        destination: 'http://localhost:8000/api/agents/:path*',
      },
    ];
  },
};

module.exports = nextConfig;
