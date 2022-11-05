<?php

use yii\db\Migration;

/**
 * Class m221104_180629_create_usuario
 */
class m221104_180629_create_usuario extends Migration
{
    /**
     * {@inheritdoc}
     */
    public function safeUp()
    {
        $this->createTable('usuarios', [
            'id' => $this->primaryKey(),
            'nome' => $this->text()->notNull(),
            'usuario' => $this->text()->notNull()->unique(),
            'senha' => $this->text()->notNull(),
        ]);

        $this->insert('usuarios', [
            'nome' => 'cerbero',
            'usuario' => 'cerbero',
            'senha' => Yii::$app->getSecurity()->generatePasswordHash('cerbero'),
        ]);

        $this->addCommentOnTable('usuarios', 'Tabela de usuários');
        $this->addCommentOnColumn('usuarios', 'id', 'Identificador do usuário');
        $this->addCommentOnColumn('usuarios', 'nome', 'Nome');
        $this->addCommentOnColumn('usuarios', 'usuario', 'Nome de usuário');
        $this->addCommentOnColumn('usuarios', 'senha', 'Senha');
    }

    /**
     * {@inheritdoc}
     */
    public function safeDown()
    {
        $this->dropTable('usuarios');
    }

    /*
    // Use up()/down() to run migration code without a transaction.
    public function up()
    {

    }

    public function down()
    {
        echo "m221104_180629_create_usuario cannot be reverted.\n";

        return false;
    }
    */
}
