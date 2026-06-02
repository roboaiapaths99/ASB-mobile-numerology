import React from 'react';
import { jsPDF } from 'jspdf';

const ResultsSection = ({ results }) => {
  if (!results) return null;

  const { client_info, moolank, bhagyank, classification, pair_analysis, final_result, interpretation, remedies } = results;

  const generateReportText = () => {
    return `ASB Numerology Report\n\n` +
      `Name: ${client_info.name}\n` +
      `Date of Birth: ${client_info.dob}\n` +
      `Mobile Number: ${client_info.mobile}\n` +
      `${client_info.challenges ? `Challenges: ${client_info.challenges}\n` : ''}\n` +
      `Core Numbers:\n` +
      `- Moolank: ${moolank}\n` +
      `- Bhagyank: ${bhagyank}\n\n` +
      `Number Classification:\n` +
      `- Friendly: ${classification.friendly.join(', ') || 'None'}\n` +
      `- Enemy: ${classification.enemy.join(', ') || 'None'}\n` +
      `- Neutral: ${classification.neutral.join(', ') || 'None'}\n\n` +
      `Pair Analysis:\n` +
      pair_analysis.map(pair => `  ${pair.serial}. ${pair.pair} — ${pair.type}`).join('\n') +
      `\n\nRemedies:\n` +
      `- Charging Direction: ${remedies.directions.join(', ')}\n` +
      `- Lucky Color: ${remedies.color_info.color} (${remedies.color_info.planet})\n` +
      `- Recommended Crystals: ${remedies.crystals.join(', ') || 'None'}\n`;
  };

  const normalizeSpacedText = (text) => {
    if (!text) return text;
    let normalized = text;
    while (/([A-Za-z])\s(?=[A-Za-z])/g.test(normalized)) {
      normalized = normalized.replace(/([A-Za-z])\s(?=[A-Za-z])/g, '$1');
    }
    return normalized;
  };

  const handleDownload = async () => {
    const doc = new jsPDF({ unit: 'pt', format: 'letter' });
    const pageWidth = doc.internal.pageSize.getWidth();
    const pageHeight = doc.internal.pageSize.getHeight();
    const margin = 40;
    const contentWidth = pageWidth - margin * 2;
    const sectionSpacing = 26;
    let cursorY = 130;
    let logoImg = null;

    // Try to load the ASB logo image
    try {
      const response = await fetch('/images/cb4c8e26-4cfb-407c-be4c-3e65d19edaa5-Photoroom.png');
      if (response.ok) {
        const blob = await response.blob();
        // Validate it's a PNG
        if (blob.type === 'image/png') {
          const reader = new FileReader();
          logoImg = await new Promise((resolve) => {
            reader.onload = () => resolve(reader.result);
            reader.onerror = () => resolve(null);
            reader.readAsDataURL(blob);
          });
        }
      }
    } catch (error) {
      console.warn('Could not load logo image, using text fallback');
    }

    const setupPage = () => {
      doc.setFillColor('#f5f1e8');
      doc.rect(0, 0, pageWidth, pageHeight, 'F');
      doc.setFillColor('#1a1a3e');
      doc.rect(0, 0, pageWidth, 110, 'F');

      // Add logo if available
      if (logoImg) {
        try {
          doc.addImage(logoImg, 'PNG', margin + 10, 18, 50, 76);
        } catch {
          // If image fails, use text fallback
          drawLogoFallback();
        }
      } else {
        // Fallback: logo text block
        drawLogoFallback();
      }

      doc.setDrawColor('#7c3aed');
      doc.setLineWidth(3);
      doc.line(margin, 112, pageWidth - margin, 112);

      doc.setTextColor('#ffffff');
      doc.setFont('helvetica', 'bold');
      doc.setFontSize(20);
      doc.text('ASB NUMEROLOGY REPORT', margin + 90, 46);
      doc.setFont('helvetica', 'normal');
      doc.setFontSize(10);
      doc.text(`Generated for: ${client_info.name}`, margin + 90, 66);
      doc.text(`Mobile: ${client_info.mobile}`, margin + 90, 80);
      doc.text(`DOB: ${client_info.dob}`, margin + 90, 94);

      cursorY = 130;
      doc.setTextColor('#1a1a3e');
    };

    const drawLogoFallback = () => {
      doc.setFillColor('#9f3bff');
      doc.roundedRect(margin + 10, 18, 56, 48, 10, 10, 'F');
      doc.setFillColor('#ffd036');
      doc.circle(margin + 38, 36, 10, 'F');
      doc.setFillColor('#ffffff');
      doc.setFont('helvetica', 'bold');
      doc.setFontSize(10);
      doc.text('ASB', margin + 17, 53);
      doc.setFont('helvetica', 'normal');
      doc.setFontSize(6);
      doc.text('Numerology', margin + 16, 60);
    };

    const addSection = (title, contentLines) => {
      if (cursorY > pageHeight - margin - 100) {
        doc.addPage();
        setupPage();
      }

      doc.setFillColor('#7c3aed');
      doc.roundedRect(margin, cursorY - 10, 160, 24, 6, 6, 'F');
      doc.setTextColor('#ffffff');
      doc.setFont('helvetica', 'bold');
      doc.setFontSize(12);
      doc.text(title, margin + 10, cursorY + 8);
      cursorY += 34;

      doc.setTextColor('#1a1a3e');
      doc.setFont('helvetica', 'normal');
      doc.setFontSize(11);
      contentLines.forEach((line) => {
        const normalized = normalizeSpacedText(line.replace(/•/g, '-'));
        const split = doc.splitTextToSize(normalized, contentWidth);
        if (cursorY + split.length * 16 > pageHeight - margin) {
          doc.addPage();
          setupPage();
          doc.setTextColor('#1a1a3e');
          doc.setFont('helvetica', 'normal');
          doc.setFontSize(11);
        }
        doc.text(split, margin, cursorY);
        cursorY += split.length * 16;
      });
      cursorY += sectionSpacing;
    };

    setupPage();

    addSection('Core Numbers', [
      `Moolank: ${moolank}`,
      `Bhagyank: ${bhagyank}`,
    ]);

    addSection('Number Classification', [
      `Friendly: ${classification.friendly.join(', ') || 'None'}`,
      `Enemy: ${classification.enemy.join(', ') || 'None'}`,
      `Neutral: ${classification.neutral.join(', ') || 'None'}`,
    ]);

    addSection('Pair Analysis', pair_analysis.map((pair) => `${pair.serial}. ${pair.pair} — ${pair.type}`));

    addSection('Remedies', [
      `Charging Direction: ${remedies.directions.join(', ')}`,
      `Lucky Color: ${remedies.color_info.color} (${remedies.color_info.planet})`,
      `Recommended Crystals: ${remedies.crystals.join(', ') || 'None'}`,
    ]);

    doc.save(`ASB_Numerology_Report_${client_info.name.replace(/\s+/g, '_')}.pdf`);
  };

  return (
    <div className="space-y-8">
      <div className="flex justify-center mb-6">
        <button type="button" onClick={() => handleDownload()} className="asb-button">
          📥 Download PDF Report
        </button>
      </div>

      {/* Personal Information */}
      <div>
        <h2 className="section-title">✨ Personal Information</h2>
        <div className="grid md:grid-cols-2 gap-4">
          <div className="result-card">
            <h4>👤 Name</h4>
            <p>{client_info.name}</p>
          </div>
          <div className="result-card">
            <h4>📅 Date of Birth</h4>
            <p>{client_info.dob}</p>
          </div>
          <div className="result-card">
            <h4>📱 Mobile Number</h4>
            <p>{client_info.mobile}</p>
          </div>
          {client_info.challenges && (
            <div className="result-card">
              <h4>🎯 Current Challenges</h4>
              <p>{client_info.challenges}</p>
            </div>
          )}
        </div>
      </div>

      {/* Core Numbers */}
      <div>
        <h2 className="section-title">✨ Core Numbers</h2>
        <div className="grid md:grid-cols-2 gap-6">
          <div className="metric-box gold">
            <h3>{moolank}</h3>
            <p>Moolank (Birth Day)</p>
          </div>
          <div className="metric-box green">
            <h3>{bhagyank}</h3>
            <p>Bhagyank (Destiny)</p>
          </div>
        </div>
      </div>

      {/* Number Classification */}
      <div>
        <h2 className="section-title">✨ Number Classification</h2>
        <div className="grid md:grid-cols-3 gap-4">
          <div className="result-card">
            <h4>✅ Friendly Numbers</h4>
            <p>{classification.friendly.join(', ') || 'None'}</p>
          </div>
          <div className="result-card">
            <h4>❌ Enemy Numbers</h4>
            <p>{classification.enemy.join(', ') || 'None'}</p>
          </div>
          <div className="result-card">
            <h4>⚖️ Neutral Numbers</h4>
            <p>{classification.neutral.join(', ') || 'None'}</p>
          </div>
        </div>
      </div>

      {/* Pair Analysis */}
      <div>
        <h2 className="section-title">✨ Pair Analysis</h2>
        <div className="table-container">
          <table className="w-full">
            <thead>
              <tr className="table-header">
                <th className="py-3 px-4">Serial</th>
                <th className="py-3 px-4">Pair</th>
                <th className="py-3 px-4">Type</th>
              </tr>
            </thead>
            <tbody>
              {pair_analysis.map((pair, index) => (
                <tr
                  key={index}
                  className={`${
                    pair.type === 'Good' 
                      ? 'table-row-good' 
                      : pair.type === 'Bad' 
                      ? 'table-row-bad' 
                      : 'table-row-neutral'
                  }`}
                >
                  <td className="py-3 px-4 text-center">{pair.serial}</td>
                  <td className="py-3 px-4 text-center">{pair.pair}</td>
                  <td className="py-3 px-4 text-center font-semibold">{pair.type}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>



      {/* Remedies */}
      <div>
        <h2 className="section-title">✨ Remedies & Recommendations</h2>
        <div className="grid md:grid-cols-3 gap-4">
          <div className="result-card">
            <h4>🧭 Charging Direction</h4>
            <p>{remedies.directions.join(', ')}</p>
          </div>
          <div className="result-card">
            <h4>🎨 Lucky Color</h4>
            <p>{remedies.color_info.color}</p>
            <p className="text-sm text-gray-500 mt-1">Planet: {remedies.color_info.planet}</p>
          </div>
          <div className="result-card">
            <h4>💎 Recommended Crystals</h4>
            <p>{remedies.crystals.join(', ') || 'None needed'}</p>
            <p className="text-sm mt-2">
              <a 
                href="https://asbcrystal.in/" 
                target="_blank" 
                rel="noopener noreferrer"
                className="text-asb-purple hover:text-asb-magenta hover:underline transition-colors"
              >
                🔮 Buy Crystals Online
              </a>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ResultsSection;
