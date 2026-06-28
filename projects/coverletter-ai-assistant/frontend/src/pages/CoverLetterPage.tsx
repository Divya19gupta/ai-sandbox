import { Box, Typography, Button } from '@mui/material';
import { useLocation, useNavigate } from 'react-router-dom';
import Navbar from '../components/Navbar';

const CoverLetterPage = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const coverLetter = location.state?.coverLetter;

  const handleCopy = () => {
    const full = `${coverLetter.header}\n\n${coverLetter.body}\n\n${coverLetter.footer}`;
    navigator.clipboard.writeText(full);
  };

  const cleanLines = (text: string) =>
    text?.split('\n').filter(line =>
      !line.toLowerCase().includes('not provided') &&
      !line.includes('[') &&
      !line.includes(']')
    ) ?? [];

  return (
    <Box sx={{ bgcolor: '#08080F', minHeight: '100vh', position: 'relative', overflow: 'hidden' }}>
      
      {/* BACKGROUND BLOBS */}
      <Box sx={{ position: 'fixed', top: -100, left: -100, width: 400, height: 400, borderRadius: '50%', background: 'radial-gradient(circle, rgba(124,58,237,0.12) 0%, transparent 70%)', pointerEvents: 'none', zIndex: 0 }} />
      <Box sx={{ position: 'fixed', bottom: -100, right: -100, width: 500, height: 500, borderRadius: '50%', background: 'radial-gradient(circle, rgba(56,189,248,0.07) 0%, transparent 70%)', pointerEvents: 'none', zIndex: 0 }} />
      <Box sx={{ position: 'fixed', top: '40%', right: '20%', width: 300, height: 300, borderRadius: '50%', background: 'radial-gradient(circle, rgba(167,139,250,0.06) 0%, transparent 70%)', pointerEvents: 'none', zIndex: 0 }} />

      <Box sx={{ position: 'relative', zIndex: 1 }}>
        <Navbar />
        <Box sx={{ px: { xs: 3, md: 6 }, py: 5, maxWidth: 900, margin: '0 auto' }}>

          {/* TOP BAR */}
          <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', mb: 4, flexWrap: 'wrap', gap: 2 }}>
            <Typography sx={{ fontSize: { xs: 18, md: 22 }, fontWeight: 800, color: '#F0EEF9' }}>
              Your cover letter is ready 🎉
            </Typography>
            <Box sx={{ display: 'flex', gap: 1.5, flexWrap: 'wrap' }}>
              <Button onClick={() => navigate('/')} sx={{ bgcolor: 'transparent', border: '1px solid #2D2A3E', color: '#A78BFA', fontWeight: 600, fontSize: 13, px: 2, py: 1, borderRadius: 2, textTransform: 'none', '&:hover': { borderColor: '#7C3AED', bgcolor: '#1A1728' } }}>
                ↩ Start over
              </Button>
              <Button onClick={handleCopy} sx={{ bgcolor: 'transparent', border: '1px solid #2D2A3E', color: '#A78BFA', fontWeight: 600, fontSize: 13, px: 2, py: 1, borderRadius: 2, textTransform: 'none', '&:hover': { borderColor: '#7C3AED', bgcolor: '#1A1728' } }}>
                📋 Copy
              </Button>
              <Button sx={{ background: 'linear-gradient(135deg,#7C3AED,#6D28D9)', color: 'white', fontWeight: 700, fontSize: 13, px: 2.5, py: 1, borderRadius: 2, textTransform: 'none', boxShadow: '0 4px 12px rgba(124,58,237,0.3)', '&:hover': { transform: 'translateY(-1px)' } }}>
                ⬇ Download PDF
              </Button>
            </Box>
          </Box>

          {/* SCORE BAR */}
          <Box sx={{ bgcolor: '#13111F', border: '1px solid #2D2A3E', borderRadius: 3, p: '20px 32px', mb: 3, display: 'flex', alignItems: 'center' }}>
            {[{ num: '94%', label: 'JD Match' }, { num: '0', label: 'Generic phrases' }, { num: 'A+', label: 'German Format' }, { num: '✓', label: 'Ready to send' }].map((s, i) => (
              <Box key={i} sx={{ display: 'flex', alignItems: 'center', flex: 1 }}>
                <Box sx={{ flex: 1, textAlign: 'center' }}>
                  <Typography sx={{ fontSize: { xs: 18, md: 24 }, fontWeight: 800, color: '#A78BFA', lineHeight: 1 }}>{s.num}</Typography>
                  <Typography sx={{ fontSize: 11, color: '#6B7280', mt: 0.5 }}>{s.label}</Typography>
                </Box>
                {i < 3 && <Box sx={{ width: '1px', height: 36, bgcolor: '#2D2A3E', flexShrink: 0 }} />}
              </Box>
            ))}
          </Box>

          {/* DOCUMENT */}
          <Box sx={{ height: '65vh', overflowY: 'auto', borderRadius: 4, boxShadow: '0 20px 60px rgba(0,0,0,0.6)', '&::-webkit-scrollbar': { width: 6 }, '&::-webkit-scrollbar-track': { bgcolor: '#13111F' }, '&::-webkit-scrollbar-thumb': { bgcolor: '#7C3AED', borderRadius: 3 } }}>
            <Box sx={{ bgcolor: 'white', borderRadius: 4, p: { xs: '32px 28px', md: '56px 72px' } }}>

              {/* HEADER — German DIN format */}
              <Box sx={{ mb: 4, pb: 3, borderBottom: '1px solid #e8e8e8' }}>
                {cleanLines(coverLetter?.header ?? '').map((line: string, i: number) => {
                  const isName = i === 0;
                  const isSubject = line.toLowerCase().startsWith('subject');
                  const isBlank = line.trim() === '';
                  return (
                    <Typography key={i} sx={{
                      fontFamily: "'Helvetica Neue', Arial, sans-serif",
                      fontSize: isName ? 16 : isSubject ? 13 : 12,
                      fontWeight: isName ? 700 : isSubject ? 700 : 400,
                      color: isName ? '#111' : isSubject ? '#1a1a1a' : '#555',
                      lineHeight: isBlank ? 1.2 : 1.7,
                      mt: isSubject ? 1.5 : 0,
                    }}>
                      {line || '\u00A0'}
                    </Typography>
                  );
                })}
              </Box>

              {/* BODY */}
              <Box sx={{ mb: 4 }}>
                {cleanLines(coverLetter?.body ?? '').map((line: string, i: number) => {
                  const isBlank = line.trim() === '';
                  return (
                    <Typography key={i} sx={{
                      fontFamily: "'Georgia', serif",
                      fontSize: 15,
                      color: '#1a1a1a',
                      lineHeight: isBlank ? 1 : 1.85,
                      mb: isBlank ? 1.5 : 0,
                    }}>
                      {line || '\u00A0'}
                    </Typography>
                  );
                })}
              </Box>

              {/* FOOTER */}
              <Box sx={{ pt: 3, borderTop: '1px solid #e8e8e8' }}>
                {cleanLines(coverLetter?.footer ?? '').map((line: string, i: number) => (
                  <Typography key={i} sx={{
                    fontFamily: "'Helvetica Neue', Arial, sans-serif",
                    fontSize: 13,
                    color: '#555',
                    lineHeight: 1.7,
                  }}>
                    {line || '\u00A0'}
                  </Typography>
                ))}
              </Box>

            </Box>
          </Box>

        </Box>
      </Box>

      <style>{`
        @keyframes breathe { 0%,100%{transform:scale(1)} 50%{transform:scale(1.05)} }
      `}</style>
    </Box>
  );
};

export default CoverLetterPage;