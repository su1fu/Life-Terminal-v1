// ui/Terminal.jsx

import React, { useState, useEffect } from 'react';

const Terminal = ({ riskData }) => {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    // 模拟系统扫描日志
    const systemLogs = [
      "INITIALIZING LIFE_TERMINAL_V1...",
      "LOADING_USER_PROFILE: " + riskData.user_id,
      "SCANNING_ASTRO_COORDINATES...",
      "CHECKING_FOUR_TRANSFORMATIONS_2026...",
      "LOGS: " + riskData.warning_msg
    ];

    systemLogs.forEach((msg, i) => {
      setTimeout(() => {
        setLogs(prev => [...prev, `> ${msg}`]);
      }, i * 600);
    });
  }, [riskData]);

  return (
    <div style={{ backgroundColor: '#000', color: '#00FF41', padding: '20px', fontFamily: 'monospace' }}>
      <div style={{ borderBottom: '1px solid #0D5330', marginBottom: '10px', fontSize: '12px' }}>
        STATUS: {riskData.level} | SYSTEM_ID: {riskData.user_id}
      </div>
      
      {logs.map((log, index) => (
        <div key={index} style={{ marginBottom: '5px', animation: 'pulse 1s' }}>
          {log}
        </div>
      ))}

      {riskData.level === 'L3_ORANGE' || riskData.level === 'L4_RED' ? (
        <div style={{ color: '#FFB100', marginTop: '20px', fontWeight: 'bold' }}>
          [!] EMERGENCY_ALERT: {riskData.commands.join(' / ')}
        </div>
      ) : null}
      
      <div className="cursor" style={{ width: '8px', height: '15px', backgroundColor: '#00FF41', display: 'inline-block' }}></div>
    </div>
  );
};

export default Terminal;
