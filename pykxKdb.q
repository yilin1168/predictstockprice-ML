import kx

# 创建连接到 5010 端口
h = kx.q.hopen(5010)

# 发送异步更新
h('.u.upd', kx.SymbolAtom('trade'), [kx.q.z.n, kx.SymbolAtom('APPL'), 35.65, 100, kx.SymbolAtom('B')])

# 关闭连接
h.close()