<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Personal Finance Advisor</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        .user-message {
            background-color: #3b82f6;
            color: white;
            border-radius: 1rem 1rem 0 1rem;
        }
        .bot-message {
            background-color: #f3f4f6;
            color: #1f2937;
            border-radius: 1rem 1rem 1rem 0;
        }
        .animate-in {
            animation: fadeIn 0.3s ease-in-out;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        #chatContainer {
            scroll-behavior: smooth;
        }
    </style>
</head>
<body class="bg-gray-100 min-h-screen flex flex-col">
    <header class="bg-blue-600 text-white p-4 shadow-md">
        <div class="container mx-auto flex justify-between items-center">
            <h1 class="text-2xl font-bold">💰 Personal Finance Advisor</h1>
            <div class="flex items-center space-x-2">
                <span class="animate-pulse w-3 h-3 rounded-full bg-green-400"></span>
                <span class="text-sm">AI Online</span>
            </div>
        </div>
    </header>

    <div class="flex-1 container mx-auto p-4 pb-20 overflow-y-auto" id="chatContainer">
        <div class="mb-4 animate-in">
            <div class="bot-message p-4 max-w-3xl inline-block">
                <p class="font-semibold">Welcome to your Personal Finance Advisor!</p>
                <p>I can help you with:</p>
                <ul class="list-disc pl-5 mt-2">
                    <li>Budgeting strategies</li>
                    <li>Expense tracking</li>
                    <li>Saving plans</li>
                    <li>Investment advice</li>
                    <li>Debt management</li>
                </ul>
                <p class="mt-2">Ask me anything about your personal finances!</p>
            </div>
        </div>
    </div>

    <div class="fixed bottom-0 left-0 right-0 bg-white border-t border-gray-300 p-4 shadow-lg">
        <div class="container mx-auto">
            <form id="chatForm" class="flex gap-2">
                <input 
                    type="text" 
                    id="userInput" 
                    placeholder="Ask about budgeting, savings, investments..." 
                    class="flex-1 p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                    autocomplete="off"
                >
                <button 
                    type="submit" 
                    class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors"
                >
                    Send
                </button>
            </form>
        </div>
    </div>

    <script>
        const chatContainer = document.getElementById('chatContainer');
        const chatForm = document.getElementById('chatForm');
        const userInput = document.getElementById('userInput');

        // Finance knowledge base
        const financeKnowledge = {
            greetings: ["Hi! How can I assist with your finances today?", "Hello! Ready to improve your financial health?"],
            budgeting: {
                tips: [
                    "The 50/30/20 rule is a great starting point: 50% needs, 30% wants, 20% savings/debt.",
                    "Track every expense for a month to identify spending patterns.",
                    "Use budgeting apps to automate tracking.",
                    "Review your budget monthly and adjust as needed."
                ],
                tools: ["Mint", "YNAB", "PocketGuard", "EveryDollar", "GoodBudget"]
            },
            saving: {
                strategies: [
                    "Pay yourself first - automate transfers to savings on payday.",
                    "Start small, even $50/month adds up.",
                    "Create specific savings goals for motivation.",
                    "Reduce unnecessary expenses and redirect to savings."
                ],
                accounts: ["High-yield savings", "Money market", "CDs", "Emergency fund"]
            },
            investing: {
                beginner: [
                    "Start with index funds for diversification.",
                    "Consider your time horizon and risk tolerance.",
                    "Tax-advantaged accounts (401k, IRA) should come first.",
                    "Dollar-cost averaging reduces timing risk."
                ],
                types: ["Stocks", "Bonds", "ETFs", "Mutual funds", "Real estate"]
            },
            debt: {
                management: [
                    "Snowball method: pay smallest debts first for motivation.",
                    "Avalanche method: pay highest interest debts first to save money.",
                    "Consider consolidation loans for multiple high-interest debts.",
                    "Negotiate lower interest rates with creditors."
                ],
                warning: "Avoid taking on new debt while paying off existing debt."
            }
        };

        // Add a message to the chat
        function addMessage(text, isUser) {
            const messageDiv = document.createElement('div');
            messageDiv.className = `mb-4 animate-in ${isUser ? 'text-right' : ''}`;
            
            const messageContent = document.createElement('div');
            messageContent.className = isUser ? 'user-message p-4 max-w-3xl inline-block' : 'bot-message p-4 max-w-3xl inline-block';
            messageContent.innerHTML = `<p>${text}</p>`;
            
            messageDiv.appendChild(messageContent);
            chatContainer.appendChild(messageDiv);
            
            // Scroll to bottom of chat
            chatContainer.scrollTop = chatContainer.scrollHeight;
            
            // Return the div for potential modifications
            return messageDiv;
        }

        // Process user input
        function processInput(input) {
            const lowerInput = input.toLowerCase();

            // Add user message first
            addMessage(input, true);
            
            // Show typing indicator
            const typingIndicator = addMessage('<div class="flex space-x-1"><div class="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></div><div class="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style="animation-delay: 0.2s"></div><div class="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style="animation-delay: 0.4s"></div></div>', false);
            
            // Simulate thinking delay
            setTimeout(() => {
                // Remove typing indicator
                typingIndicator.remove();
                
                let response = "";
                
                // Generate response based on input
                if (lowerInput.includes("hello") || lowerInput.includes("hi")) {
                    const greetings = financeKnowledge.greetings;
                    response = greetings[Math.floor(Math.random() * greetings.length)];
                } 
                else if (lowerInput.includes("budget") || lowerInput.includes("spend")) {
                    const tips = financeKnowledge.budgeting.tips;
                    const randomTip = tips[Math.floor(Math.random() * tips.length)];
                    response = `Budgeting tip: ${randomTip}\n\nRecommended tools: ${financeKnowledge.budgeting.tools.join(", ")}`;
                }
                else if (lowerInput.includes("save") || lowerInput.includes("savings")) {
                    const strategies = financeKnowledge.saving.strategies;
                    const randomStrategy = strategies[Math.floor(Math.random() * strategies.length)];
                    response = `Saving strategy: ${randomStrategy}\n\nAccount types to consider: ${financeKnowledge.saving.accounts.join(", ")}`;
                }
                else if (lowerInput.includes("invest") || lowerInput.includes("stock")) {
                    const beginnerTips = financeKnowledge.investing.beginner;
                    const randomTip = beginnerTips[Math.floor(Math.random() * beginnerTips.length)];
                    response = `Investment advice: ${randomTip}\n\nCommon investment types: ${financeKnowledge.investing.types.join(", ")}`;
                }
                else if (lowerInput.includes("debt") || lowerInput.includes("loan")) {
                    const management = financeKnowledge.debt.management;
                    const randomTip = management[Math.floor(Math.random() * management.length)];
                    response = `Debt management: ${randomTip}\n\nWarning: ${financeKnowledge.debt.warning}`;
                }
                else {
                    response = "I'm your personal finance assistant. Could you please rephrase your question? I can help with budgeting, saving, investing, or debt management advice.";
                }
                
                // Add response to chat
                addMessage(response, false);
                
            }, 1000 + Math.random() * 1000); // Random delay between 1-2 seconds
        }

        // Handle form submission
        chatForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const input = userInput.value.trim();
            
            if (input) {
                processInput(input);
                userInput.value = '';
            }
            
            // Focus the input field again
            userInput.focus();
        });

        // Allow pressing Enter to submit (but keep Shift+Enter for new lines)
        userInput.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                chatForm.dispatchEvent(new Event('submit'));
            }
        });
    </script>
</body>
</html>
