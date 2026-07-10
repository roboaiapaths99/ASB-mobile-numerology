import React, { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { MessageSquare, X, RotateCcw, Send, Calendar, Sparkles } from 'lucide-react';

/* ──────────────────────────────────────────────
   Inline-style chatbot – no Tailwind required
   ────────────────────────────────────────────── */

const S = {
    /* Floating button */
    fab: {
        position: 'fixed', bottom: 24, right: 24, zIndex: 9999,
        width: 56, height: 56, borderRadius: '50%',
        background: 'linear-gradient(135deg, #7c3aed, #ec4899, #f59e0b)',
        color: '#fff', border: 'none', cursor: 'pointer',
        display: 'flex', alignItems: 'center', justifyContent: 'center',
        boxShadow: '0 8px 24px rgba(124,58,237,.35)',
    },
    fabPing: {
        position: 'absolute', inset: 0, borderRadius: '50%',
        background: 'rgba(124,58,237,.2)',
        animation: 'chatbot-ping 2s cubic-bezier(0,0,.2,1) infinite',
    },
    /* Panel */
    panel: {
        position: 'fixed', bottom: 96, right: 24, zIndex: 9999,
        width: 380, maxWidth: 'calc(100vw - 2rem)',
        height: 560, maxHeight: 'calc(100vh - 8rem)',
        display: 'flex', flexDirection: 'column',
        background: 'rgba(255,255,255,.97)', backdropFilter: 'blur(16px)',
        borderRadius: 24, overflow: 'hidden',
        border: '1px solid rgba(124,58,237,.08)',
        boxShadow: '0 20px 60px rgba(124,58,237,.12)',
    },
    /* Header */
    header: {
        background: 'linear-gradient(135deg, #7c3aed, #db2777)',
        padding: '14px 16px', color: '#fff',
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
    },
    headerLeft: { display: 'flex', alignItems: 'center', gap: 8 },
    headerIcon: {
        padding: 5, background: 'rgba(255,255,255,.12)',
        borderRadius: '50%', border: '1px solid rgba(255,255,255,.2)',
        display: 'flex', alignItems: 'center', justifyContent: 'center',
    },
    headerTitle: { fontWeight: 700, fontSize: 13, letterSpacing: 1, textTransform: 'uppercase', margin: 0 },
    headerSub: { fontSize: 10, color: 'rgba(255,255,255,.7)', display: 'flex', alignItems: 'center', gap: 6, margin: 0 },
    onlineDot: { width: 6, height: 6, borderRadius: '50%', background: '#4ade80', display: 'inline-block', animation: 'chatbot-ping 2s infinite' },
    headerBtns: { display: 'flex', gap: 4 },
    headerBtn: {
        background: 'none', border: 'none', color: 'rgba(255,255,255,.8)',
        cursor: 'pointer', padding: 6, borderRadius: 8,
    },
    /* Progress */
    progressTrack: { width: '100%', height: 3, background: 'rgba(124,58,237,.06)', position: 'relative', overflow: 'hidden' },
    progressBar: { height: '100%', background: 'linear-gradient(90deg,#fbbf24,#7c3aed)', transition: 'width .5s ease-out' },
    /* Messages */
    msgArea: { flex: 1, overflowY: 'auto', padding: 16, display: 'flex', flexDirection: 'column', gap: 12, background: 'rgba(255,247,237,.05)' },
    msgRow: (isUser) => ({ display: 'flex', flexDirection: 'column', alignItems: isUser ? 'flex-end' : 'flex-start', gap: 4 }),
    bubble: (isUser) => ({
        padding: '12px 14px', maxWidth: '85%', fontSize: 12, lineHeight: 1.65, fontWeight: 500,
        borderRadius: isUser ? '16px 4px 16px 16px' : '4px 16px 16px 16px',
        background: isUser ? 'linear-gradient(135deg,#7c3aed,#ec4899)' : '#fff',
        color: isUser ? '#fff' : '#1e293b',
        border: isUser ? 'none' : '1px solid rgba(124,58,237,.06)',
        boxShadow: '0 2px 6px rgba(0,0,0,.04)',
    }),
    stepBadge: { fontSize: 8, fontWeight: 700, color: '#7c3aed', background: 'rgba(124,58,237,.08)', padding: '2px 8px', borderRadius: 20, textTransform: 'uppercase', letterSpacing: 1 },
    btnWrap: { display: 'flex', flexWrap: 'wrap', gap: 6, paddingTop: 4, maxWidth: '90%' },
    optBtn: {
        padding: '6px 12px', background: '#fff', color: '#7c3aed',
        border: '1px solid rgba(124,58,237,.12)', borderRadius: 20,
        fontSize: 11, fontWeight: 700, cursor: 'pointer',
        boxShadow: '0 1px 3px rgba(0,0,0,.04)',
    },
    serviceGrid: { display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8, paddingTop: 8, width: '100%' },
    serviceCard: {
        padding: '8px 12px', background: '#fff', border: '1px solid rgba(124,58,237,.06)',
        borderRadius: 12, fontSize: 10, fontWeight: 700, textAlign: 'center',
        color: '#334155', textDecoration: 'none', cursor: 'pointer',
        boxShadow: '0 1px 3px rgba(0,0,0,.04)',
    },
    /* Typing */
    typingWrap: { display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4 },
    typingBubble: {
        padding: '12px 14px', background: '#fff', border: '1px solid rgba(124,58,237,.06)',
        borderRadius: '4px 16px 16px 16px', boxShadow: '0 2px 6px rgba(0,0,0,.04)',
        display: 'flex', alignItems: 'center', gap: 6,
    },
    typingText: { fontSize: 10, color: '#94a3b8', fontWeight: 600, fontStyle: 'italic' },
    dot: (delay) => ({
        width: 6, height: 6, borderRadius: '50%', background: 'rgba(124,58,237,.35)',
        animation: 'chatbot-bounce .6s ease-in-out infinite', animationDelay: `${delay}ms`,
    }),
    /* Footer */
    footer: {
        padding: 12, background: '#fff', borderTop: '1px solid rgba(124,58,237,.06)',
        display: 'flex', alignItems: 'center', gap: 8,
    },
    input: {
        flex: 1, padding: '10px 14px', fontSize: 12, fontWeight: 500,
        border: '1px solid rgba(124,58,237,.1)', borderRadius: 12,
        outline: 'none', color: '#1e293b', background: '#fff',
    },
    sendBtn: {
        padding: 10, borderRadius: 12, border: 'none', cursor: 'pointer',
        background: 'linear-gradient(135deg,#7c3aed,#ec4899)', color: '#fff',
        boxShadow: '0 4px 12px rgba(124,58,237,.25)',
        display: 'flex', alignItems: 'center', justifyContent: 'center',
    },
};

/* keyframes injected once */
const KEYFRAMES = `
@keyframes chatbot-ping{0%{transform:scale(1);opacity:1}75%,100%{transform:scale(1.6);opacity:0}}
@keyframes chatbot-bounce{0%,100%{transform:translateY(0)}50%{transform:translateY(-4px)}}
`;

const Chatbot = ({ user, token }) => {
    const [isOpen, setIsOpen] = useState(false);
    const [messages, setMessages] = useState([]);
    const [inputText, setInputText] = useState('');
    const [inputType, setInputType] = useState('text');
    const [inputPlaceholder, setInputPlaceholder] = useState('Type here...');
    const [isTyping, setIsTyping] = useState(false);
    const [stepInfo, setStepInfo] = useState({ step: 0, total_steps: 6 });
    const chatEndRef = useRef(null);
    const styleInjected = useRef(false);

    const API_BASE = window.location.hostname.includes('asbreports.in')
        ? 'https://api.asbreports.in'
        : `http://${window.location.hostname}:8001`;

    /* inject keyframes once */
    useEffect(() => {
        if (!styleInjected.current) {
            const tag = document.createElement('style');
            tag.textContent = KEYFRAMES;
            document.head.appendChild(tag);
            styleInjected.current = true;
        }
    }, []);

    const getSessionId = () => {
        let sid = sessionStorage.getItem('asb_chat_session_id');
        if (!sid) {
            sid = 'sess_' + Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
            sessionStorage.setItem('asb_chat_session_id', sid);
        }
        return sid;
    };

    useEffect(() => {
        if (chatEndRef.current) chatEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }, [messages, isTyping]);

    useEffect(() => {
        const saved = localStorage.getItem('asb_chat_history');
        const savedMode = localStorage.getItem('asb_chat_input_mode');
        const savedStep = localStorage.getItem('asb_chat_step');
        if (saved) {
            try {
                const parsed = JSON.parse(saved);
                setMessages(parsed.map(msg => ({
                    ...msg,
                    text: msg.text || ''
                })));
            } catch (e) {
                console.error(e);
            }
        }
        if (savedMode) try { const m = JSON.parse(savedMode); setInputType(m.inputType || 'text'); setInputPlaceholder(m.inputPlaceholder || 'Type here...'); } catch (e) { /* */ }
        if (savedStep) try { setStepInfo(JSON.parse(savedStep)); } catch (e) { /* */ }
    }, []);

    const persistState = (msgs, type, ph, step) => {
        localStorage.setItem('asb_chat_history', JSON.stringify(msgs));
        localStorage.setItem('asb_chat_input_mode', JSON.stringify({ inputType: type, inputPlaceholder: ph }));
        localStorage.setItem('asb_chat_step', JSON.stringify(step));
    };

    const initChat = async (forceReset = false) => {
        setIsTyping(true);
        const welcome = `🙏 Namaste! Welcome to ASB AI Advisor.\n\nI'm your AI Numerology Expert.\n\nI'll guide you step-by-step to provide personalized numerology insights based on your details.\n\nLet's begin.`;
        let initial = [];
        if (!forceReset) {
            initial = [{ sender: 'bot', text: welcome }];
            setMessages(initial);
        }
        try {
            const sid = getSessionId();
            let userProfile = null;
            if (user && user.name && user.dob && user.name !== 'User' && user.dob !== '01-01-1970') {
                userProfile = { name: user.name, dob: user.dob, gender: user.gender || 'Other' };
            }
            const res = await fetch(`${API_BASE}/api/chatbot/chat`, {
                method: 'POST', headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: 'start', session_id: sid, user_profile: userProfile })
            });
            const data = await res.json();
            const updated = [...initial, { sender: 'bot', text: data.answer, buttons: data.buttons || null, type: data.type || null, services: data.services || null }];
            const ns = { step: data.step || 0, total_steps: data.total_steps || 6 };
            setMessages(updated); setInputType(data.input_type || 'text'); setInputPlaceholder(data.placeholder || 'Type here...'); setStepInfo(ns);
            persistState(updated, data.input_type || 'text', data.placeholder || 'Type here...', ns);
        } catch (err) {
            console.error(err);
            const errMsgs = [...initial, { sender: 'bot', text: '⚠️ Unable to connect to ASB AI server. Please check your internet connection and try again.' }];
            setMessages(errMsgs);
        } finally { setIsTyping(false); }
    };

    useEffect(() => { if (isOpen && messages.length === 0) initChat(); }, [isOpen]);

    const handleReset = () => {
        localStorage.removeItem('asb_chat_history'); localStorage.removeItem('asb_chat_input_mode'); localStorage.removeItem('asb_chat_step');
        sessionStorage.removeItem('asb_chat_session_id');
        setMessages([]); setInputType('text'); setInputPlaceholder('Type here...'); setStepInfo({ step: 0, total_steps: 6 });
        setTimeout(() => initChat(true), 100);
    };

    const handleSendMessage = async (msgText) => {
        if (!msgText.trim()) return;
        const updated = [...messages, { sender: 'user', text: msgText }];
        setMessages(updated); setInputText(''); setInputType('button_only'); setIsTyping(true);
        try {
            const sid = getSessionId();
            let userProfile = null;
            if (user && user.name && user.dob) userProfile = { name: user.name, dob: user.dob, gender: user.gender || 'Other' };
            const res = await fetch(`${API_BASE}/api/chatbot/chat`, {
                method: 'POST', headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: msgText, session_id: sid, user_profile: userProfile })
            });
            const data = await res.json();
            const final = [...updated, { sender: 'bot', text: data.answer, buttons: data.buttons || null, type: data.type || null, services: data.services || null }];
            const ns = { step: data.step || 0, total_steps: data.total_steps || 6 };
            setMessages(final); setInputType(data.input_type || 'text'); setInputPlaceholder(data.placeholder || 'Type here...'); setStepInfo(ns);
            persistState(final, data.input_type || 'text', data.placeholder || 'Type here...', ns);
        } catch (err) {
            console.error(err);
            setMessages([...updated, { sender: 'bot', text: '⚠️ Connection lost. Unable to fetch guidance.' }]);
            setInputType('text');
        } finally { setIsTyping(false); }
    };

    const handleKeyPress = (e) => { if (e.key === 'Enter') handleSendMessage(inputText); };
    const progressPercent = stepInfo.step && stepInfo.total_steps ? (stepInfo.step / stepInfo.total_steps) * 100 : 0;

    return (
        <>
            {/* Floating Launcher */}
            <motion.button
                onClick={() => setIsOpen(!isOpen)}
                style={S.fab}
                whileHover={{ scale: 1.08 }}
                whileTap={{ scale: 0.95 }}
            >
                <AnimatePresence mode="wait">
                    {isOpen ? (
                        <motion.span key="close" initial={{ rotate: -90, opacity: 0 }} animate={{ rotate: 0, opacity: 1 }} exit={{ rotate: 90, opacity: 0 }} transition={{ duration: 0.2 }}>
                            <X size={24} />
                        </motion.span>
                    ) : (
                        <motion.span key="chat" initial={{ scale: 0.5, opacity: 0 }} animate={{ scale: 1, opacity: 1 }} exit={{ scale: 0.5, opacity: 0 }} transition={{ duration: 0.2 }}
                            style={{ position: 'relative', display: 'flex', alignItems: 'center', justifyContent: 'center', width: '100%', height: '100%' }}>
                            <MessageSquare size={24} />
                            <span style={S.fabPing}></span>
                        </motion.span>
                    )}
                </AnimatePresence>
            </motion.button>

            {/* Chat Panel */}
            <AnimatePresence>
                {isOpen && (
                    <motion.div
                        initial={{ opacity: 0, y: 50, scale: 0.95 }}
                        animate={{ opacity: 1, y: 0, scale: 1 }}
                        exit={{ opacity: 0, y: 50, scale: 0.95 }}
                        transition={{ type: 'spring', damping: 25, stiffness: 200 }}
                        style={S.panel}
                    >
                        {/* Header */}
                        <div style={S.header}>
                            <div style={S.headerLeft}>
                                <div style={S.headerIcon}><Sparkles size={16} color="#fbbf24" /></div>
                                <div>
                                    <h3 style={S.headerTitle}>ASB AI Advisor</h3>
                                    <p style={S.headerSub}><span style={S.onlineDot}></span> Online • Numerology Expert</p>
                                </div>
                            </div>
                            <div style={S.headerBtns}>
                                <button onClick={handleReset} title="Reset chat" style={S.headerBtn}><RotateCcw size={16} /></button>
                                <button onClick={() => setIsOpen(false)} style={S.headerBtn}><X size={16} /></button>
                            </div>
                        </div>

                        {/* Progress */}
                        {stepInfo.step > 0 && stepInfo.step <= stepInfo.total_steps && (
                            <div style={S.progressTrack}><div style={{ ...S.progressBar, width: `${progressPercent}%` }}></div></div>
                        )}

                        {/* Messages */}
                        <div style={S.msgArea}>
                            {messages.map((msg, i) => (
                                <div key={i} style={S.msgRow(msg.sender === 'user')}>
                                    {msg.sender === 'bot' && msg.step && msg.total_steps && msg.step <= msg.total_steps && (
                                        <span style={S.stepBadge}>Step {msg.step} of {msg.total_steps}</span>
                                    )}
                                    <div style={S.bubble(msg.sender === 'user')} dangerouslySetInnerHTML={{ __html: (msg.text || '').replace(/\n/g, '<br/>') }}></div>
                                    {msg.buttons && (
                                        <div style={S.btnWrap}>
                                            {msg.buttons.map((b, j) => (
                                                <button key={j} onClick={() => handleSendMessage(b)} style={S.optBtn}>{b}</button>
                                            ))}
                                        </div>
                                    )}
                                    {msg.type === 'service_cards' && msg.services && (
                                        <div style={S.serviceGrid}>
                                            {msg.services.map((s, j) => (
                                                <a key={j} href={s.url} target="_blank" rel="noopener noreferrer" style={S.serviceCard}>{s.title}</a>
                                            ))}
                                        </div>
                                    )}
                                </div>
                            ))}
                            {isTyping && (
                                <div style={S.typingWrap}>
                                    <div style={S.typingBubble}>
                                        <span style={S.typingText}>Preparing guidance</span>
                                        <div style={{ display: 'flex', gap: 4 }}>
                                            <span style={S.dot(0)}></span>
                                            <span style={S.dot(150)}></span>
                                            <span style={S.dot(300)}></span>
                                        </div>
                                    </div>
                                </div>
                            )}
                            <div ref={chatEndRef} />
                        </div>

                        {/* Input Footer */}
                        <div style={S.footer}>
                            {inputType === 'date' ? (
                                <div style={{ flex: 1, position: 'relative', display: 'flex', alignItems: 'center' }}>
                                    <input type="date" value={inputText} onChange={(e) => setInputText(e.target.value)} onKeyPress={handleKeyPress} style={S.input} />
                                    <Calendar size={14} style={{ position: 'absolute', right: 12, color: 'rgba(124,58,237,.35)', pointerEvents: 'none' }} />
                                </div>
                            ) : (
                                <input type="text" value={inputText} onChange={(e) => setInputText(e.target.value)} onKeyPress={handleKeyPress}
                                    placeholder={inputPlaceholder} disabled={inputType === 'button_only'}
                                    style={{ ...S.input, ...(inputType === 'button_only' ? { background: '#f8fafc', color: '#94a3b8', cursor: 'not-allowed' } : {}) }} />
                            )}
                            <button onClick={() => handleSendMessage(inputText)} disabled={inputType === 'button_only' || !inputText.trim()}
                                style={{ ...S.sendBtn, ...(inputType === 'button_only' || !inputText.trim() ? { opacity: 0.4, cursor: 'not-allowed' } : {}) }}>
                                <Send size={14} />
                            </button>
                        </div>
                    </motion.div>
                )}
            </AnimatePresence>
        </>
    );
};

export default Chatbot;
